class GraphDestination:

    def __init__(self, name, distance, time):
        self.name = name
        self.distance = distance
        self.time = time

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.distance == other.distance and self.time == other.time
        else:
            return False