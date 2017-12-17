import csv
from datetime import datetime

stop_start_time = []

file_name = 'bar_bjelopolje.csv'
#file_name = 'podgorica_niksic.csv'

with open(file_name, newline='', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')
    for row in file_reader:
        #print(', '.join(row))
        stop_start = '2017-12-16 ' + row[1] + ':00'
        stop_start_time.append(stop_start)

print(stop_start_time)

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

episode_durations = []
counter = 0
for started_time in stop_start_time:
    if counter > 0:
        previous_time = stop_start_time[counter-1]
        time_difference = datetime.strptime(started_time, TIME_FORMAT) - datetime.strptime(previous_time, TIME_FORMAT)
        episode_durations.append(str(time_difference))
    counter += 1

print(episode_durations)
print(min(episode_durations))
print(max(episode_durations))

# file_path = 'bar_bjelopolje.csv'
# with open(file_path) as fp:
#     line = fp.readline()
#     cnt = 1
#     while line:
#         print("Line {}: {}".format(cnt, line.strip()))
#         line = fp.readline()
#         cnt += 1


journey_start_date = "2017-12-16 05:25:00"
journey_end_date = "2017-12-16 06:22:00"
number_of_stops = 10

stop_times = [7, 6, 4, 4, 6, 4, 9, 9, 5]

#print(sum(stop_times))

start_latency = 0
end_latency = 7


class Journey:
    pass

class SimulateTrainData:
    number_of_journeys = 0

