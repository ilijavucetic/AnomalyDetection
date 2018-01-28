import copy

#sequences_2 = [[['1', '2'], ['3']], [['1', '2'], ['4']], [['1', '2'], ['3']], [['1', '2'], ['4']], [['1'], ['3'], ['1']], [['1'], ['3', '4']], [['1', '3'], ['5']], [['1', '3'], ['5']], [['1'], ['3', '4']], [['2'], ['3'], ['1']], [['2'], ['3', '4']], [['2'], ['3', '5']], [['2'], ['3', '4']], [['2'], ['3', '5']]]

#sequences_2 = [[['1', '2'], ['3']],  [['2'], ['3', '4']]]
#sequences_2 = [[['2'], ['3'], ['1']]]

#sequences_2 = [['1', '2'], [['1'], ['3']], ['1', '3'], [['1'], ['4']], [['1'], ['5']], [['2'], ['3']], [['2'], ['4']], [['2'], ['5']], [['3'], ['1']], ['3', '4'], [['3'], ['5']], ['3', '5']]
#sequences_2 = [['1', '2'], [['1'], ['3']], ['1', '3'], [['1'], ['4']], [['1'], ['5']], [['2'], ['3']], [['2'], ['4']], [['2'], ['5']], [['3'], ['1']], ['3', '4'], [['3'], ['5']], ['3', '5']]
sequences_2 = [[['2'],  ['3', '4']]]

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


def get_new_sequence(s1, s2):

    s1_t = copy.deepcopy(s1)
    s2_t = copy.deepcopy(s2)
    s1_length = len(s1_t)

    s3 = []

    if isinstance(s2_t[0], list) and len(s2_t[0]) == 1:

        s1_last = s1_t[-1]
        s2_first = s2_t[0]

        #if isinstance(s1_last, list) and isinstance(s2_first, list):
        if isinstance(s2_t[0], list) and len(s2_t[0]) == 1:
            temp = s2_t[s1_length-1:]
            s3 = s1_t + temp
        else:
            s3.append(s1_t)
            temp = s2_t[s1_length-1:]
            for elem in temp:
                s3.append(elem)
    else:
        s3 = []
        last_elem = s1_t[-1]
        merged = []

        if isinstance(last_elem, list):
            for temp12 in s2_t:
                if temp12 not in merged:
                    merged.append(temp12)

            for t in s1_t[:-1]:
                s3.append(t)
            #length = len(s3)
            s3.append(merged)
            #s3[length] = sorted(s3[length])
        else:
            temp = s2_t[1:]
            s3 = s1_t + temp
    return s3


for sequence in sequences_2:

    sequence_length = len(sequence)

    first = sequence[0]
    last = sequence[sequence_length-1]

    sequence_key = to_string(sequence)

    cross_table[sequence_key] = {}
    cross_table[sequence_key]["minus_first"] = []
    cross_table[sequence_key]["minus_last"] = []

    single_mesure = True
    print("sequence", sequence)
    for seq in sequence:
        if isinstance(seq, list):
            single_mesure = False

    if single_mesure:
        for seq in sequence:
            temp_array = copy.deepcopy(sequence)
            temp_array.remove(seq)
            cross_table[sequence_key]["minus_first"].append(temp_array)
            cross_table[sequence_key]["minus_last"].append(temp_array)
    else:
        if len(first) > 1:
            for i in range(0, len(first)):
                temp_array = copy.deepcopy(first)
                temp_array.remove(first[i])

                first_temp = []

                first_temp.append(temp_array)
                for j in range(1, sequence_length):
                    first_temp.append(sequence[j])

                cross_table[sequence_key]["minus_first"].append(first_temp)

        elif len(first) == 1:
            temp_array = copy.deepcopy(sequence)
            #print("temp_array", temp_array)
            temp_array.pop(0)
            if len(temp_array) == 1:
                temp_array = temp_array[0]

            #print(temp_array)
            cross_table[sequence_key]["minus_first"].append(temp_array)
            pass

        if len(last) > 1:
            temp_array = []
            for i in range(0, len(last)):
                temp_array = copy.deepcopy(last)
                temp_array.remove(last[i])

                first_temp = []

                for j in range(0, sequence_length-1):
                    print(1)
                    first_temp.append(sequence[j])

                first_temp.append(temp_array)
                print(first_temp)
                cross_table[sequence_key]["minus_last"].append(first_temp)

        elif len(last) == 1:
            temp_array = copy.deepcopy(sequence)
            temp_array.pop(sequence_length-1)
            if len(temp_array) == 1:
                temp_array = temp_array[0]
            cross_table[sequence_key]["minus_last"].append(temp_array)
            pass

print("cross_table ", cross_table)

for sequence in sequences_2:
    key = to_string(sequence)

    sequence_minus_first = cross_table[key]["minus_first"]

    for sequence_other in sequences_2:
        lenth_other = len(sequence_other)
        key_other = to_string(sequence_other)

        if key != key_other:

            sequence_other_minus_last = cross_table[key_other]["minus_last"]
            break_outer = False
            for first in sequence_minus_first:
                if break_outer:
                    break

                for last in sequence_other_minus_last:

                    # TODO CHECK
                    first = sorted(first)
                    last = sorted(last)

                    if first == last:

                        print("1", sequence)
                        print("2", sequence_other)
                        temp = get_new_sequence(sequence, sequence_other)

                        print("res", temp)
                        if temp not in generated_sequence:
                            generated_sequence.append(temp)

                        break_outer = True
                        break

print("generated_sequence", generated_sequence)
