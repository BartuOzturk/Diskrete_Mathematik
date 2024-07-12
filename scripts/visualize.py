import matplotlib.pyplot as plt
import osmnx as ox


def plot_path(graph, path, start_node, end_node):
    """
   Visualisiert einen Pfad auf einem Straßennetz.

   Args:
       graph (networkx.MultiDiGraph): Der Graph des Straßennetzes.
       path (list of int): Liste der Knoten-IDs, die den Pfad darstellen.
       start_node (int): Knoten-ID des Startpunkts.
       end_node (int): Knoten-ID des Endpunkts.
   """
    fig, ax = ox.plot_graph_route(graph, path, route_color='y', route_linewidth=6, node_size=10)
    plt.show()
