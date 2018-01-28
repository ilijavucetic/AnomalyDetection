import copy

sequences_2 = [[['1', '2'], ['3']], [['1', '2'], ['4']], [['1', '2'], ['3']], [['1', '2'], ['4']], [['1'], ['3'], ['1']], [['1'], ['3', '4']], [['1', '3'], ['5']], [['1', '3'], ['5']], [['1'], ['3', '4']], [['2'], ['3'], ['1']], [['2'], ['3', '4']], [['2'], ['3', '5']], [['2'], ['3', '4']], [['2'], ['3', '5']]]

#sequences_2 = [[['1', '2'], ['3']],  [['2'], ['3', '4']]]

generated_sequence = []
cross_table = {}


def to_string(sequences):
    string = ""
    if isinstance(sequences[0], list):
        for sequence in sequences:
            string += "( "
            for sequence_elements in sequence:
                string += sequence_elements
            string += " )"
    else:
        string = ','.join(sequences)
        string = "( " + string + " )"
    return string

for sequence in sequences_2:

    first = sequence[0]
    second = sequence[1]

    sequence_key = to_string(sequence)

    cross_table[sequence_key] = {}
    cross_table[sequence_key]["first"] = []
    cross_table[sequence_key]["second"] = []

    if len(first) > 1:
        for i in range(0, len(first)):
            temp_array = copy.deepcopy(first)
            temp_array.remove(first[i])
            #print("temp_array", temp_array)

            first_temp = []
            first_temp.append(temp_array)
            first_temp.append(second)

            cross_table[sequence_key]["first"].append(first_temp)

    elif len(first) == 1:
        first1 = first[0]
        cross_table[sequence_key]["first"].append(first)
        pass

    if len(second) > 1:
        for i in range(0, len(second)):
            temp_array = copy.deepcopy(second)
            temp_array.remove(second[i])

            first_temp = []

            first_temp.append(first)
            first_temp.append(temp_array)
            cross_table[sequence_key]["second"].append(first_temp)

    elif len(second) == 1:
        cross_table[sequence_key]["second"].append(first)
        pass







# if isinstance(first, list):
    #     first = first[0]
    #     second = sequence[1][0]
    #     cross_table[sequence_key]["first"].append(second)
    #     cross_table[sequence_key]["second"].append(first)
    #     pass




    # if isinstance(first, list):
    # if len(first) > 1:
    #
    #     cross_table[sequence_key]["first"].append(first)
    #     cross_table[sequence_key]["first"].append(second)
    #     cross_table[sequence_key]["second"].append(first)
    #     cross_table[sequence_key]["second"].append(second)
    # else:
    #     first = first[0]
    #     second = sequence[1][0]
    #     cross_table[sequence_key]["first"].append(second)
    #     cross_table[sequence_key]["second"].append(first)
    #     pass
    #
    # if len(second) > 1:
    #     cross_table[sequence_key]["first"].append(first)
    #     cross_table[sequence_key]["first"].append(second)
    #     cross_table[sequence_key]["second"].append(first)
    #     cross_table[sequence_key]["second"].append(second)
    # else:
    #     second = sequence[1][0]
    #     cross_table[sequence_key]["first"].append(second)
    #     cross_table[sequence_key]["second"].append(first)
    #     pass




# exit()

print("cross_table ", cross_table)

for sequence in sequences_2:
    key = to_string(sequence)

    sequence_minus_first = cross_table[key]["first"]

    for sequence_other in sequences_2:
        lenth_other = len(sequence_other)
        key_other = to_string(sequence_other)

        if key != key_other:

            sequence_other_minus_last = cross_table[key_other]["second"]
            break_outer = False
            for first in sequence_minus_first:
                if break_outer:
                    break

                for last in sequence_other_minus_last:

                    print("First", first)
                    print("LAST", last)

                    # if first == last:
                    #     temp = get_new_sequence(sequence, sequence_other)
                    #
                    #     generated_sequence.append(temp)
                    #
                    #     break_outer = True
                    #     break

print("generated_sequence", generated_sequence)
