import numpy as np


def floyd_warshall(num_vertices, edge_list):
    """
    Implementiert den Floyd-Warshall-Algorithmus zur Berechnung der kürzesten Pfade zwischen allen Paaren von Knoten.

    Args:
    num_vertices (int): Anzahl der Knoten im Graph.
    edge_list (list of tuples): Liste der Kanten des Graphen, wobei jede Kante als Tupel (src, dest, weight) dargestellt ist.

    Returns:
    np.array: Eine Matrix, die die kürzeste Distanz zwischen allen Paaren von Knoten darstellt.
    """
    # Initialisiere die Distanzmatrix mit unendlich, außer der Diagonalen (Distanz zu sich selbst ist 0)
    dist = np.full((num_vertices, num_vertices), np.inf)
    np.fill_diagonal(dist, 0)

    # Gewichte der Kanten im Graph eintragen
    for src, dest, weight in edge_list:
        dist[src][dest] = weight

    # Durchführung des Floyd-Warshall-Algorithmus
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Aktualisiere die Distanzmatrix mit dem kürzeren Weg, wenn gefunden
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
