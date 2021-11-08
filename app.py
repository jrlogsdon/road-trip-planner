import distance_matrix_csv_writer
import google_distance_matrix_service
import user

api_key = input("Enter your Google API Key containing access to Distance Matrix API: ")

locations = user.get_locations()

distance_url = google_distance_matrix_service.build_distance_url(locations, locations, key=api_key)

dest_matrix = google_distance_matrix_service.get_distance_matrix_from_api(distance_url)

distance_matrix_csv_writer.write_csv(dest_matrix, "anotherone.csv")

