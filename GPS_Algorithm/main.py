__author__ = 'Ilija_V_ITS'
import csv
from datetime import datetime, timedelta

file_name = 'C:/Users/Ilija_V_ITS/PycharmProjects/AnomalyDetection/GPS_Algorithm/transactions.csv'

dict_list = {}

with open(file_name, newline='', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')
    first = True
    for row in file_reader:
        if first:
            first = False
            continue

        transaction_time = row[0]
        customer_id = row[1]
        items = row[2]

        if len(items) > 1:
            items = '(' + items + ')'

        current_list = dict_list.get(customer_id)
        #print(current_list)

        if current_list is None:
            dict_list[customer_id] = [items]
        else:
            #print(111111111)
            #print(dict_list[customer_id])
            #print(items)
            dict_list[customer_id].append(items)
            #print(dict_list[customer_id])
            pass
            #print(dict_list[customer_id])
            #print(items
            # print(customer_id)
            # print(dict_list[customer_id])
            # dict_list[customer_id] = dict_list[customer_id].append(items)
            # print(dict_list[customer_id])
print(dict_list)

file_write = csv.writer(open('user_transaction.csv', 'w', newline=''), delimiter=',')

for key, value in dict_list.items():

    list_string = ''.join(value)
    file_write.writerow([key, list_string])

