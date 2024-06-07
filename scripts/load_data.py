import osmnx as ox


def load_osm_data(place_name="Biesdorf, Berlin, Germany"):
    """
    Lädt das Straßennetz eines bestimmten Ortes mithilfe von OSMnx.

    Args:
    place_name (str): Der Name des Ortes, für den das Straßennetz geladen wird.

    Returns:
    networkx.Graph: Ein Graph, der das Straßennetz des angegebenen Ortes darstellt.
    """
    # Laden des Straßennetzes für den angegebenen Ort mit dem Straßentyp 'drive'
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph
