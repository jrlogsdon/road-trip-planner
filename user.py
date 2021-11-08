

def get_locations():
    locations = []
    location = 'not_empty'
    while is_valid(location):
        location = str(input("Enter location you'd like to visit (enter no or newline to stop entering locations): "))
        if is_valid(location):
            locations.append(location)
    return locations


def is_valid(location):
    return location != '' and location != 'n' and location != 'No' and location != 'N' and location != 'no'