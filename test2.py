import csv
from datetime import datetime, timedelta
import random
from collections import OrderedDict
from SimulateTemperature.simulate_temperature import SimulateTemperatures

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

    journey_end = None

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
        self.generate_raw_data()
        #print(self.duration)
        #print(self.average_speed)

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
        self.journey_end = end
        duration = self.calculate_time_difference_in_hours(end, start)
        return duration

    def generate_raw_data(self):
        start_date_string = self.journey_start
        start_date = datetime.strptime(start_date_string, '%Y-%m-%d %H:%M:%S')
        end_date_string = self.journey_end
        end_date = datetime.strptime(end_date_string, '%Y-%m-%d %H:%M:%S')

        temp_date = start_date

        #print(temp_date)
        print("START", start_date)
        print("END", end_date)
        #print(self.input_data)
        current_route = 0

        file_write = csv.writer(open('row_data', 'w', newline=''), delimiter=',')

        file_write.writerow(["Date",
                             "Speed", "Acceleration", "Temperature"])

        while temp_date <= end_date:
            arrival_timing = datetime.strptime(self.input_data[current_route]['arrival'], '%Y-%m-%d %H:%M:%S')
            departure_timing = datetime.strptime(self.input_data[current_route]['departure'], '%Y-%m-%d %H:%M:%S')

            arrival_timing_deceleration = arrival_timing - timedelta(minutes=1)
            #arrival_timing_acceleration = arrival_timing + timedelta(minutes=1)

            #departure_timing_deceleration = departure_timing - timedelta(minutes=1)
            departure_timing_acceleration = departure_timing + timedelta(minutes=1)

            speed = None
            acceleration = None
            temparature = None

            print("temp_date", temp_date)
            print("arrival", arrival_timing)
            print("departure", departure_timing)

            speed = None
            acceleration = None
            temparature = None
            print(temp_date)
            temperature_object = SimulateTemperatures(temp_date)
            random_temperature = temperature_object.get_radom_temperature()

            # TODO SIMULATE RANDOM VALUE AND ADD HUMIDITY IF NECESSARY
            # STOP
            if arrival_timing <= temp_date <= departure_timing:
                speed = 0
                acceleration = 0
                temperature = random_temperature
            # DEPARTURE ACCELERATION
            elif departure_timing < temp_date < departure_timing_acceleration:
                speed = 20
                acceleration = 20
                temperature = random_temperature + 2
            # ARRIVAL DECELERATION
            elif arrival_timing_deceleration < temp_date < arrival_timing:
                speed = 20
                acceleration = -20
                temperature = random_temperature + 10
            else:
                # TODO GENERATE RANDOM SPEED AND Acceleration
                speed = 40
                acceleration = 0
                temperature = random_temperature + 5

            # if speed is not None:
            #     print(speed)`
            #     print(acceleration)

            file_write.writerow([temp_date,
                                 speed, acceleration, temperature])

            temp_date = temp_date + timedelta(minutes=1)
            if temp_date > departure_timing:
                current_route += 1





        data = []

        #file_write = csv.writer(open('row_data', 'w', newline=''), delimiter=',')

        # while temp_date < end_date:
        #
        #     for i in range(len(self.input_data)):
        #         arrival_timing = datetime.strptime(self.input_data[i]['arrival'], '%Y-%m-%d %H:%M:%S')
        #         departure_timing = datetime.strptime(self.input_data[i]['departure'], '%Y-%m-%d %H:%M:%S')
        #
        #         arrival_timing_deceleration = arrival_timing - timedelta(minutes=1)
        #         #arrival_timing_acceleration = arrival_timing + timedelta(minutes=1)
        #
        #         #departure_timing_deceleration = departure_timing - timedelta(minutes=1)
        #         departure_timing_acceleration = departure_timing + timedelta(minutes=1)
        #
        #         speed = None
        #         acceleration = None
        #         temparature = None
        #
        #         # STOP
        #         if arrival_timing <= temp_date <= departure_timing:
        #             speed = 0
        #             acceleration = 0
        #             temperature = 25
        #         # DEPARTURE ACCELERATION
        #         elif departure_timing < temp_date < departure_timing_acceleration:
        #             speed = 20
        #             acceleration = 20
        #             temperature = 63
        #         # ARRIVAL DECELERATION
        #         elif arrival_timing_deceleration < temp_date < arrival_timing:
        #             speed = 20
        #             acceleration = -20
        #             temperature = 53
        #         else:
        #             speed = 40
        #             acceleration = 0
        #             temperature = 44
        #
        #         # if speed is not None:
        #         #     print(speed)
        #         #     print(acceleration)
        #
        #         file_write.writerow([self.input_data[i]['arrival'], self.input_data[i]['departure'],
        #                              speed, acceleration, temperature])
        #     temp_date = temp_date + timedelta(minutes=5)

start_dates = ['19:59', '06:40']

now = datetime.now()
current_date = now.strftime("%Y-%m-%d ")

#journey_start = current_date + start_dates[0] + ':00'
journey_start = '2017-12-16 08:20:00'
x = BarBp(journey_start)