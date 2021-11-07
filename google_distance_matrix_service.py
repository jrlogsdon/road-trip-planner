import requests
import URLify

base_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial"

def build_distance_url(origins, destinations, key):
    start = urlifyList(origins)
    end = urlifyList(destinations)
    return base_url + "&origins=" + start + "&destinations=" + end + "&key=" + key


def urlifyList(list_of_strings):
    url = ""
    for string in list_of_strings:
        url += URLify.URLIfy(string) + "|"
    return url[:-1]



def get_distance_matrix_from_api(distance_url):
    print("making google mapis api request to:", distance_url)
    response = requests.get(distance_url).json()
    print("response from API call:", response['status'])
    return response


