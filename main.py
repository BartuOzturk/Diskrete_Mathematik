from scripts.load_data import load_osm_data
from scripts.floyd_warshall import floyd_warshall
from scripts.visualize import plot_distance_matrix
import networkx as nx
import matplotlib.pyplot as plt

def convert_graph_to_edge_list(graph):
    edge_list = []
    node_id_map = {}
    next_index = 0

    for u, v, data in graph.edges(data=True):
        if u not in node_id_map:
            node_id_map[u] = next_index
            next_index += 1
        if v not in node_id_map:
            node_id_map[v] = next_index
            next_index += 1

        u_mapped = node_id_map[u]
        v_mapped = node_id_map[v]
        weight = data.get('length', 1)  # Standardgewicht, falls 'length' nicht verfügbar ist
        edge_list.append((u_mapped, v_mapped, weight))

    num_vertices = next_index  # Anzahl der einzigartigen Knoten
    return edge_list, num_vertices

def draw_network(graph):
    print("Zeichne das Netzwerkdiagramm...")
    pos = nx.spring_layout(graph)  # Positionen der Knoten im 2D-Raum
    nx.draw_networkx_nodes(graph, pos, node_size=10, node_color='blue', alpha=0.6)
    nx.draw_networkx_edges(graph, pos, alpha=0.4)
    plt.title('Netzwerkdiagramm')
    plt.show()

def main():
    print("Laden des Graphen...")
    graph = load_osm_data()

    print("Zeichne das Netzwerkdiagramm...")
    draw_network(graph)

    print("Konvertiere Graph zu Edge List...")
    edge_list, num_vertices = convert_graph_to_edge_list(graph)
    print("Anzahl der Knoten:", num_vertices)
    print("Anzahl der Kanten:", len(edge_list))

    print("Berechne Distanzen mit Floyd-Warshall...")
    distances = floyd_warshall(num_vertices, edge_list)
    print("Distanzmatrix berechnet.")

    print("Visualisiere die Distanzmatrix...")
    plot_distance_matrix(distances)
    print("Visualisierung abgeschlossen.")

if __name__ == "__main__":
    main()
