import distance_matrix_csv_writer
import explorer
import google_distance_matrix_service
import parse_response_to_graph
import user

api_key = input("Enter your Google API Key containing access to Distance Matrix API: ")

locations = user.get_locations()

distance_url = google_distance_matrix_service.build_distance_url(locations, locations, key=api_key)

dest_matrix = google_distance_matrix_service.get_distance_matrix_from_api(distance_url)

graph = parse_response_to_graph.create_graph(dest_matrix)

order_to_visit_nodes = explorer.explore(graph=graph, starting_location=dest_matrix['origin_addresses'][0])

print("Most efficient way to visit nodes: \n", order_to_visit_nodes)

distance_matrix_csv_writer.write_csv(dest_matrix, "anotherone.csv")

