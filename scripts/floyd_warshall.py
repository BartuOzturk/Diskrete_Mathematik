import numpy as np


def floyd_warshall(num_vertices, edge_list):
    """
    Implementiert den Floyd-Warshall-Algorithmus zur Berechnung der kürzesten Pfade
    zwischen allen Paaren von Knoten und speichert Vorgänger für die Pfadrekonstruktion.

    Args:
        num_vertices (int): Anzahl der Knoten im Graphen.
        edge_list (list of tuple): Liste der Kanten im Format (Quellknoten, Zielknoten, Gewicht).

    Returns:
        tuple: Zwei Matrizen - die Distanzmatrix und die Vorgängermatrix.
    """
    dist = np.full((num_vertices, num_vertices), np.inf)
    pred = np.full((num_vertices, num_vertices), -1)
    np.fill_diagonal(dist, 0)

    for src, dest, weight in edge_list:
        dist[src][dest] = weight
        pred[src][dest] = src

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    print("Distanz-Matrix:")
    print(dist)
    print("Vorgänger-Matrix:")
    print(pred)

    return dist, pred
