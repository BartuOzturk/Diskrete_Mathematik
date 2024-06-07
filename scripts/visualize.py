import matplotlib.pyplot as plt
import numpy as np


def plot_distance_matrix(distances):
    """
    Visualisiert die Distanzmatrix als Heatmap.
    """
    plt.imshow(distances, cmap='hot', interpolation='nearest')
    plt.colorbar()  # Füge eine Farblegende hinzu
    plt.show()  # Zeige das Diagramm an


def plot_adjacency_matrix(matrix, title="Adjazenzmatrix"):
    """
    Visualisiert eine Adjazenzmatrix mit matplotlib.
    """
    fig, ax = plt.subplots()
    cax = ax.matshow(matrix, cmap='Blues')
    fig.colorbar(cax)
    plt.title(title)
    plt.show()
