# Node object used to coordinate the BFS
# Should have current associated distance, nodes visited, neighboring nodes, and name

class Node:

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __init__(self, name, destinations, distance=0):
        assert(isinstance(destinations, list))
        self.distance = distance
        self.name = name
        self.destinations = destinations

    def add_adjacent_node(self, node):
        self.destinations.append(node)


