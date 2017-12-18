import csv
from datetime import datetime, timedelta
import random
from collections import OrderedDict

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

    distance = 500
    duration = None
    average_speed = 0

    max_start_latency = 5 * 60
    max_end_latency = 45 * 60
    min_stop_duration = 60
    max_stop_duration = 30 * 60
    input_data = []

    output_file = "bar_beograd_output.csv"

    def __init__(self, journey_start):
        self.journey_start = journey_start
        self.load_data()
        self.write_file()
        self.duration = self.calculate_journey_duration()
        self.average_speed = self.calculate_average_speed()
        print(self.duration)
        print(self.average_speed)


    def calculate_average_speed(self):
        s = self.distance
        t = self.duration
        speed = self.distance/float(t)
        return speed

    def load_data(self):
        file_name = 'bar_beograd.csv'

        arrival_times = []
        departure_times = []

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',')
            for row in file_reader:
                stop = '2017-12-16 ' + row[1] + ':00'
                go = '2017-12-16 ' + row[2] + ':00'
                temp = {'arrival': stop, 'departure': go, 'place': row[0]}
                self.input_data.append(temp)
                arrival_times.append(stop)
                departure_times.append(go)

        time_format = '%Y-%m-%d %H:%M:%S'

        episode_durations = []
        stops_durations = []

        for i in range(len(self.input_data)):

            arrival_timing = self.input_data[i]['arrival']
            departure_timing = self.input_data[i]['departure']

            if i > 0:
                # previous_arrival_timing = arrival_times[i-1]
                previous_departure_timing = self.input_data[i-1]['departure']

                episode_duration = self.calculate_time_difference(arrival_timing, previous_departure_timing)
                self.input_data[i]['episode_duration'] = episode_duration
                #episode_durations.append(episode_duration)

                stop_duration = self.calculate_time_difference(departure_timing, arrival_timing)
                self.input_data[i]['stop_duration'] = stop_duration
                #stops_durations.append(stop_duration)

        #print(input_data)
        self.distribute_end_latency(20, len(self.input_data))

        # print(episode_durations)
        # print(len(episode_durations))
        # print(min(episode_durations))
        # print(max(episode_durations))
        #
        # print(stops_durations)
        # print(min(stops_durations))
        # print(max(stops_durations))

    @staticmethod
    def calculate_time_difference(start_time, end_time, time_format='%Y-%m-%d %H:%M:%S'):
        return str(datetime.strptime(start_time, time_format) - datetime.strptime(end_time, time_format))

    @staticmethod
    def calculate_time_difference_in_hours(start_time, end_time, time_format='%Y-%m-%d %H:%M:%S'):
        diff = datetime.strptime(start_time, time_format) - datetime.strptime(end_time, time_format)
        days = diff.days
        diff_btw_two_times = diff.seconds / 3600
        days_to_hours = days * 24
        overall_hours = days_to_hours + diff_btw_two_times
        return str(overall_hours)

    @staticmethod
    def add_seconds(time, seconds, time_format='%Y-%m-%d %H:%M:%S'):
        return str(datetime.strptime(time, time_format) + timedelta(seconds=seconds))

    @staticmethod
    def randomize_latency(latency, stops):
        dict_list = {}
        sum_latency = 0

        while sum_latency < latency * 60:
            for i in range(len(stops)):
                if sum_latency > latency * 60:
                    break
                # latency_array.append(sum_latency)
                get_latency = random.randrange(30, 60 * 3)
                sum_latency += get_latency
                key = stops[i] + 1
                dict_list[key] = get_latency
        return OrderedDict(sorted(dict_list.items()))

    def distribute_end_latency(self, latency, number_of_stops):

        stop_latency = latency / 3
        travel_latency = latency * 2 / 3
        stops = list(range(number_of_stops))
        random.shuffle(stops)
        dict_stop_list = self.randomize_latency(stop_latency, stops)
        random.shuffle(stops)
        dict_travel_list = self.randomize_latency(travel_latency, stops)

        self.add_latency(dict_stop_list)
        self.add_latency(dict_travel_list)
    #def make_stop(self):

    def add_latency(self, latency_dict):
        sum_stop_latency = 0
        any_stop_is_late = False
        is_first = True
        for i in range(len(self.input_data)):
            departure_time = self.input_data[i]['departure']
            arrival_time = self.input_data[i]['arrival']
            for index, latency in latency_dict.items():
                if i == index:
                    sum_stop_latency += latency
                    print(sum_stop_latency)
                    any_stop_is_late = True
                    break

            if any_stop_is_late:
                new_departure = self.add_seconds(departure_time, sum_stop_latency)
                self.input_data[i]['departure'] = new_departure

                if not is_first:
                    new_arrival = self.add_seconds(arrival_time, sum_stop_latency)
                    self.input_data[i]['arrival'] = new_arrival

                is_first = False

    def write_file(self):
        file_write = csv.writer(open(self.output_file, 'w', newline=''), delimiter=',')
        #file_write.writerow(['Spam'] * 5 + ['Baked Beans'])
        #file_write.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

        for i in range(len(self.input_data)):
            file_write.writerow([self.input_data[i]['arrival'],
                                 self.input_data[i]['departure']])

    def calculate_journey_duration(self):
        start = self.input_data[0]['departure']
        end = self.input_data[len(self.input_data)-1]['arrival']
        duration = self.calculate_time_difference_in_hours(end, start)
        return duration

start_dates = ['19:59', '06:40']

now = datetime.now()
current_date = now.strftime("%Y-%m-%d ")

journey_start = current_date + start_dates[0] + ':00'

x = BarBp(journey_start)