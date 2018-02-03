import calendar
from datetime import datetime, timedelta
import random


class SimulateTemperatures:

    months = range(1, 12)
    min_temperature = [1, 2, 6, 9, 13, 17, 20, 19, 16, 11, 6, 2]
    max_temperature = [9, 11, 15, 19, 23, 28, 32, 32, 27, 21, 15, 10]
    avg_temperature = []

    offset = 2

    humidity_mx = 80
    humidity_min = 45

    random_temperature = None

    def __init__(self, date):
        self.calculate_average()

        # time_format = '%Y-%m-%d %H:%M:%S'
        # date = datetime.strptime(input_date, time_format)

        month = date.month
        month_index = month - 1

        hour = date.hour

        if 7 < hour < 21:
            #print("Get random min temperature")
            temperature = self.min_temperature[month_index]

        elif 11 < hour < 15:
           #print("Get random max temperature")
            temperature = self.max_temperature[month_index]
        else:
            #print("Get random average temperature")
            temperature = self.avg_temperature[month_index]

        #print(temperature)
        self.random_temperature = random.randrange(temperature-self.offset, temperature+self.offset)
        # for month_number in self.months:
        #     print(calendar.month_name[month_number])
    pass

    def calculate_average(self):
        for i in range(1, 13):
            index = i - 1
            self.avg_temperature.append(int((self.min_temperature[index] + self.max_temperature[index]) / 2))

    def get_radom_temperature(self):
        return self.random_temperature

if __name__ == "__main__":

    date_string = '2017-12-16 21:20:00'

    for i in range(1, 100):
        temperature = SimulateTemperatures(date_string)
        random_temperature = temperature.get_radom_temperature()
        print(random_temperature)



