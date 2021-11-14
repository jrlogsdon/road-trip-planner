import node
import graphdestination


# take in a response, as a json and convert it over to a graph
# it should have a starting location as well as Destinations based off the destination object
def create_graph(response):
    graph = {}
    origins = response['origin_addresses']
    destinations = response['destination_addresses']
    rows = response['rows']
    for origin_index in range(len(origins)):
        graph_destinations = []
        for dest_index in range(len(destinations)):
            dist_val = get_distance_value(rows, origin_index, dest_index)
            duration_val = get_duration_value(rows, origin_index, dest_index)
            visiting = destinations[dest_index]
            dest = graphdestination.GraphDestination(name=visiting, distance=dist_val, time=duration_val)
            graph_destinations.append(dest)
        graph[origins[origin_index]] = node.Node(origins[origin_index], graph_destinations)
    return graph

def get_duration_value(rows, origin_index, destination_index):
    return rows[origin_index]['elements'][destination_index]['duration']['value']


def get_distance_value(rows, origin_index, destination_index):
    return rows[origin_index]['elements'][destination_index]['distance']['value']
