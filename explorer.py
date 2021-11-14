import heapq


# graph is made up of dict {location: [destinations],...} where destination holds distance/time
def explore(graph, starting_location):

    number_of_places_to_explore = len(graph[starting_location].destinations)
    queue = []
    start_location = ExploreLocation(location=starting_location, time_spent_traveling=0,
                                     previous_locations=[starting_location])
    visited = {}
    heapq.heappush(queue, start_location)
    while len(queue) != 0:
        current_place = heapq.heappop(queue)
        current_previous_locations = current_place.previous_locations
        current_time_traveling = current_place.time_spent_traveling
        if len(current_previous_locations) == number_of_places_to_explore:
            return current_previous_locations

        for destination in graph[current_place.location].destinations:
            loc = destination.name
            if current_place not in visited and loc not in current_previous_locations:
                time = current_time_traveling + destination.time
                visited_places = current_previous_locations.copy()
                visited_places.append(loc)
                explore_place = ExploreLocation(location=loc, time_spent_traveling=time,
                                                previous_locations=visited_places)
                heapq.heappush(queue, explore_place)
    return []


class ExploreLocation:

    def __init__(self, location, time_spent_traveling, previous_locations):
        self.location = location
        self.time_spent_traveling = time_spent_traveling
        self.previous_locations = previous_locations

    def __lt__(self, other):
        return self.time_spent_traveling < other.time_spent_traveling

