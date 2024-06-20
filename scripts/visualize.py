import matplotlib.pyplot as plt
import osmnx as ox


def plot_path(graph, path, start_node, end_node):
    """
    Visualisiert einen Pfad auf einem Straßennetz.
    """
    fig, ax = ox.plot_graph_route(graph, path, route_color='y', route_linewidth=6, node_size=10)
    plt.show()
