from datetime import timedelta

# allow for easy check of order, note getting rid of 's' as it isn't needed
time_units = ['day','hour', 'min']


def convert(input):
    current_time = {time : 0 for time in time_units}
    for time in time_units:
        if is_available(input, time):
            t = get_time(input, time)
            current_time[time] = t
            input = remove_used_time_unit_if_available(input)
    return timedelta(minutes=current_time['min'], hours=current_time['hour'], days=current_time['day'])


# need to handle used time units for later parsing
def remove_used_time_unit_if_available(input):
    first_space = input.find(' ')
    second_space = input.find(' ', first_space + 1)
    if second_space > 0:
        input = input[second_space + 1:]
    return input


def get_time(input, time):
    return int(input[:input.index(time) - 1])


def is_available(input, time):
    return input.find(time) >= 0
