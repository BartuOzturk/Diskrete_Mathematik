from scripts.load_data import load_osm_data, get_nearest_node
from scripts.floyd_warshall import floyd_warshall
from scripts.visualize import plot_path


def reconstruct_path(predecessors, start_index, end_index, node_id_map):
    """
     Rekonstruiert den Pfad von start_index zu end_index anhand der Vorgängermatrix.
     Übersetzt indizierte Knoten zurück zu ihren originalen IDs für die Visualisierung.

     Args:
         predecessors (list of list of int): Vorgängermatrix, die den kürzesten Pfad angibt.
         start_index (int): Index des Startknotens.
         end_index (int): Index des Endknotens.
         node_id_map (dict): Mapping von Knoten-IDs zu Indizes.

     Returns:
         list of int: Liste der originalen Knoten-IDs, die den Pfad darstellen.
     """
    path = []
    current = end_index
    while current != start_index:
        if current == -1:
            return []  # Ein Pfad existiert nicht
        path.append(current)
        current = predecessors[start_index][current]
    path.append(start_index)
    path.reverse()  # Pfad umkehren, um ihn von Start zu Ziel darzustellen
    # Übersetzen der indizierten Knoten zurück zu ihren originalen IDs
    original_path = [list(node_id_map.keys())[list(node_id_map.values()).index(node)] for node in path]
    return original_path


def main():
    """
    Hauptfunktion des Skripts. Lädt den Graphen, berechnet die kürzesten Pfade und visualisiert
    den kürzesten Pfad zwischen zwei gegebenen Adressen in Berlin.
    """
    print("Laden des Graphen für Berlin...")
    graph = load_osm_data()

    print("Anzahl der Knoten im Graph:", len(graph.nodes()))
    print("Anzahl der Kanten im Graph:", len(graph.edges()))

    start_address = "Skalitzer Straße 48, 10997 Berlin"
    end_address = "Kopischstraße 9, 10965 Berlin"
    start_node = get_nearest_node(graph, start_address)
    end_node = get_nearest_node(graph, end_address)

    # Erstelle ein Mapping von Knoten-IDs zu Indizes
    node_id_map = {node: idx for idx, node in enumerate(graph.nodes())}
    num_vertices = len(node_id_map)
    edge_list = [(node_id_map[u], node_id_map[v], data['length']) for u, v, data in graph.edges(data=True, keys=False)]

    print("Starte Berechnung des kürzesten Pfads mit Floyd-Warshall-Algorithmus...")
    distances, predecessors = floyd_warshall(num_vertices, edge_list)

    # Pfad von Start- zu Endknoten rekonstruieren und visualisieren
    path = reconstruct_path(predecessors, node_id_map[start_node], node_id_map[end_node], node_id_map)
    print("Visualisierung des Pfades läuft...")
    plot_path(graph, path, start_node, end_node)


if __name__ == "__main__":
    main()
