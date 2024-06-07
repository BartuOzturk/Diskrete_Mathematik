import matplotlib.pyplot as plt


def plot_distance_matrix(distances):
    """
    Visualisiert die Distanzmatrix als Heatmap.

    Args:
    distances (np.array): Eine Matrix, die die kürzesten Distanzen zwischen allen Knoten enthält.
    """
    # Erstelle eine Heatmap aus der Distanzmatrix
    plt.imshow(distances, cmap='hot', interpolation='nearest')
    plt.colorbar()  # Füge eine Farblegende hinzu
    plt.show()  # Zeige das Diagramm an
