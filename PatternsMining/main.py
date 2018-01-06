from pymining import itemmining, assocrules, perftesting
import csv

def get_my_transactions():
    '''Returns a small list of transactions. For testing purpose.'''
    return (
        ('A0T2', 'A1T2S0'),
        ('A1T2', 'A1T2S1'),
        ('A1T3', 'A1T2S0'),
        ('A1T2S0', 'A1T2'),
        ('A1T3', 'A1T2S1')
    )
    return (
        ('A1', 'T2'),
        ('A1', 'T2', 'S0'),
        ('A1', 'T2'),
        ('A1', 'T2', 'S0'),
        ('A1', 'T2'),
        ('A1', 'T2', 'S0'),
        ('A1', 'T2', 'S0'),
        ('A1', 'T2', 'S0'),
        ('A1', 'T2'),
        ('A1', 'T2', 'S0')
    )


# with open('../row_data', newline='', encoding='utf-8') as csvfile:
#     file_reader = csv.reader(csvfile, delimiter=',')
#     for row in file_reader:
#         data_list = (row[2], row[3], row[4])
#         print(row[2])


# transactions = perftesting.get_default_transactions()
transactions = get_my_transactions()

#print(transactions)
#transactions = transactions
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=0.2)
rules = assocrules.mine_assoc_rules(item_sets, min_support=0.2, min_confidence=0.5)
print(rules)

