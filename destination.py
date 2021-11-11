from datetime import timedelta
import time_to_date_time_converter

class Destination:

    def __init__(self, name, distance, time):
        self.name = name
        self.time = time_to_date_time_converter.convert(time)
        self.distance = distance