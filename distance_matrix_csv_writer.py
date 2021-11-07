import csv
import uuid
import os


def write_csv(distance_matrix, file_name=(str(uuid.uuid4()) + ".csv")):
    print("writing csv file to", os.getcwd(), file_name)
    with open(file_name, 'w', newline='') as csvfile:
        headers = get_headers(distance_matrix)
        rows = get_rows(distance_matrix)
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)


def get_headers(distance_matrix):
    headers = ["Name Of Starting Place"]
    for dest in distance_matrix['destination_addresses']:
        headers += [dest.split(',')[0]]
    return headers


def get_rows(distance_matrix):
    # need pointer for current origin address which also accesses that element
    rows = []
    for i in range(len(distance_matrix['origin_addresses'])):
        starting_location = distance_matrix['origin_addresses'][i].split(',')[0]
        row = [starting_location]
        for dest in distance_matrix['rows'][i]['elements']:
            distance_time = dest['distance']['text'] + "   " + dest['duration']['text']
            row.append(distance_time)
        rows.append(row)
    return rows