from geopy.geocoders import Nominatim
import osmnx as ox
import ssl
import certifi


def load_osm_data(place_name="Kreuzberg, Berlin, Germany"):
    """
    Lädt das Straßennetz eines bestimmten Ortes mithilfe von OSMnx.
    """
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph


def geocode_address(address):
    ctx = ssl.create_default_context(cafile=certifi.where())
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Benutze einen spezifischen User-Agent
    geolocator = Nominatim(user_agent="SpecificAppNameOrYourEmailHere", ssl_context=ctx)
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None, None


def get_nearest_node(graph, address):
    """
    Ermittelt den dem gegebenen Adresse nächstgelegenen Knoten im Graph.
    """
    latitude, longitude = geocode_address(address)
    nearest_node = ox.nearest_nodes(graph, longitude, latitude)
    return nearest_node
