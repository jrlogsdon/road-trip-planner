

def get_locations():
    locations = []
    location = 'not_empty'
    is_first = True
    while is_valid(location):
        if is_first:
            location = str(input("Enter a starting location: "))
            if is_valid(location):
                locations.append(location)
                is_first = False
        else:
            location = str(input("\nEnter location you'd like to visit (enter no or newline to stop entering destinations): "))
            if is_valid(location):
                locations.append(location)
    return locations


def is_valid(location):
    return location != '' and location != 'n' and location != 'No' and location != 'N' and location != 'no'