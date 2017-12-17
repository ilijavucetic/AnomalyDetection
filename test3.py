import random

#print(random.randrange(10))
from datetime import datetime, timedelta

max_start_latency = 5
max_end_latency = 45

min_stop_duration = 1
max_stop_durationmax_stop_duration = 30
max_stop_duration_2 = 15
max_stop_duration_3 = 10
max_stop_duration_4 = 5


def generate_latency(percent, min_latency, max_latency):
    random_number = random.randrange(1, 101)

    percentage = 100 - percent
    print(random_number)
    if random_number >= percentage:
        random_latency = random.randrange(min_latency, max_latency)
        print(random_latency)
        return random_latency


def randomize_latency(latency, stops):
    dict_list = []
    sum_latency = 0

    while sum_latency < latency * 60:
        for i in range(len(stops)):
            if sum_latency > latency * 60:
                break
            # latency_array.append(sum_latency)
            get_latency = random.randrange(30, 60 * 3)
            sum_latency += get_latency

            temp = {'index': stops[i]+1, 'latency': get_latency}
            dict_list.append(temp)
    return dict_list


def distribute_end_latency(latency, number_of_stops):

    stop_latency = latency/3
    travel_latency = latency*2/3
    stops = list(range(number_of_stops))
    random.shuffle(stops)
    dict_list = randomize_latency(stop_latency, stops)
    random.shuffle(stops)
    dict_travel_list = randomize_latency(travel_latency, stops)
    print(dict_list)
    print(dict_travel_list)

#distribute_end_latency(20, 19)

dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
dt = dt + timedelta(seconds=60)
print(dt)