from geopy.geocoders import Nominatim
import osmnx as ox

def load_osm_data(place_name="Kreuzberg, Berlin, Germany"):
    """
   Lädt das Straßennetz eines bestimmten Ortes mithilfe von OSMnx.

   Args:
       place_name (str): Name des Ortes, für den das Straßennetz geladen werden soll.

   Returns:
       networkx.MultiDiGraph: Der geladene Graph des Straßennetzes.
   """
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph


def geocode_address(address):
    """
    Geokodiert eine Adresse in Breiten- und Längengrade.

    Args:
        address (str): Die zu geokodierende Adresse.

    Returns:
        tuple: Breiten- und Längengrad der Adresse.
    """
    # Benutze einen spezifischen User-Agent
    geolocator = Nominatim(user_agent="SpecificAppNameOrYourEmailHere")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None, None


def get_nearest_node(graph, address):
    """
     Ermittelt den dem gegebenen Adresse nächstgelegenen Knoten im Graph.

     Args:
         graph (networkx.MultiDiGraph): Der Graph des Straßennetzes.
         address (str): Die Adresse, für die der nächste Knoten ermittelt werden soll.

     Returns:
         int: Knoten-ID des dem gegebenen Adresse nächstgelegenen Knotens.
     """
    latitude, longitude = geocode_address(address)
    nearest_node = ox.nearest_nodes(graph, longitude, latitude)
    return nearest_node
