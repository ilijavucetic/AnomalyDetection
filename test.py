import csv
from datetime import datetime
#import datetime
# file_name = 'train_bjelo_polje_data'
#
# with open(file_name, newline='', encoding='utf-8') as csvfile:
#     file_data = csv.reader(csvfile, delimiter=',')
#     for row in file_data:
#         print(row)
#         #stop_start = '2017-12-16 ' + row[1] + ':00'

start_dates = ['06:55', '09:10', '18:57']

now = datetime.now()
current_date = now.strftime("%Y-%m-%d ")
#print(current_date)

journey_start = current_date + start_dates[0] + ':00'

#print(journey_start)

max_start_latency = 5
max_end_latency = 45


# class BarBp:
#     number_of_stops = 32
#
#     def __int__(self, journey_test):
#         self.journey_test = journey_test
#         file_name = 'bar_bjelopolje.csv'
#
#         with open(file_name, newline='', encoding='utf-8') as csvfile:
#             file_reader = csv.reader(csvfile, delimiter=',')
#             for row in file_reader:
#                 print(', '.join(row))
#                 # stop_start = '2017-12-16 ' + row[1] + ':00'
#
# journey1 = BarBp(journey_start)

class BarBp:
    def __init__(self, journey_start):
        self.journey_start = journey_start
        self.load_data()

    def load_data(self):
        file_name = 'bar_bjelopolje.csv'

        stop_start_time = []

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',')
            for row in file_reader:
                #print(', '.join(row))
                stop_start = '2017-12-16 ' + row[1] + ':00'
                stop_start_time.append(stop_start)

        time_format = '%Y-%m-%d %H:%M:%S'

        episode_durations = []
        counter = 0
        for started_time in stop_start_time:
            if counter > 0:
                previous_time = stop_start_time[counter - 1]
                time_difference = datetime.strptime(started_time, time_format) - datetime.strptime(previous_time,
                                                                                                   time_format)
                episode_durations.append(str(time_difference))
            counter += 1

        print(episode_durations)
        print(len(episode_durations))
        print(min(episode_durations))
        print(max(episode_durations))

    #def make_stop(self):



x = BarBp(journey_start)