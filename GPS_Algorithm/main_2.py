# h (1, 2) (3) i h (1, 2) (3, 4) i h (1, 2) (3, 4) i
# h (1, 2) (4) i h (1, 2) (3) (5) i
# h (1) (3, 4) i
# h (1, 3) (5) i
# h (2) (3, 4) i
# h (2) (3) (5) i


def get_sequence_ellements(sequences):


    items = []

    for sequence in sequences:
        for sequence_elements in sequence:
            for element in sequence_elements:
                if element not in items:
                    items.append(element)

    return items


def calculate_support(items, sequences):
    items_support = {}

    for item in items:
        items_support[item] = 0
        for sequence in sequences:
            for sequence_elements in sequence:
                if item in sequence_elements:
                    items_support[item] += 1
                    break
    return items_support


def generate_sequence_2(items, sequences):
    possible_sequences = []

    for item_first in items:
        for item_second in items:
            if item_first == item_second:

                pattern = [[item_first], [item_second]]
                is_valid = check_support(pattern, sequences)
                #print(is_valid)
                if check_support(pattern, sequences):
                    possible_sequences.append(pattern)
            else:
                pattern1 = [[item_first], [item_second]]
                pattern2 = [item_first, item_second]

                is_valid_1 = check_support(pattern1, sequences)
                is_valid_2 = check_support(pattern2, sequences)
                #print(is_valid_1)
                #print(is_valid_2)
                if check_support(pattern1, sequences):
                    possible_sequences.append(pattern1)
                if check_support(pattern2, sequences):
                    possible_sequences.append(pattern2)

    return possible_sequences


def generate_sequence_3(items, sequences_2):

    sequence_3 = []

    cross_table = {}

    for sequence in sequences_2:

        first = sequence[0]

        sequence_key = to_string(sequence)

        cross_table[sequence_key] = {}
        cross_table[sequence_key]["first"] = []
        cross_table[sequence_key]["second"] = []

        #print(sequence_key)

        if isinstance(first, list):
            first = first[0]
            second = sequence[1][0]
            cross_table[sequence_key]["first"].append(second)
            cross_table[sequence_key]["second"].append(first)
            pass
        # Multiple choices
        else:
            second = sequence[1]

            cross_table[sequence_key]["first"].append(first)
            cross_table[sequence_key]["first"].append(second)
            cross_table[sequence_key]["second"].append(first)
            cross_table[sequence_key]["second"].append(second)

            pass

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

                        if first == last:
                            #print("First ", sequence)
                            #print("Second ", sequence_other)
                            #print(sequence_other[lenth_other-1])

                            temp = get_new_sequence(sequence, sequence_other)
                            sequence_3.append(temp)

                            break_outer = True
                            break

                # if sequence_minus_first == sequence_other_minus_last:
                #     print(sequence)
                #     print(sequence_other_minus_last)



    for key, value in cross_table.items():
        pass

        # print(first)
        # print(second)


    #print(sequences_2)
    print(sequence_3)
    #print(cross_table)


def get_new_sequence(s1, s2):
    #print("S1", s1)
    #print("S2", s2)

    if isinstance(s2[len(s2) - 1], list):
        s3 = [s1]
        s3 += s2[1:]
        #print("Seperate")
    else:
        #print("Together")

        #print(s1+s3)

        s3 = s1[:]
        temp = s2[1:]
        for elem in temp:
            s3.append(elem)
    #print(s3)
    return s3


def check_support(check_sequence, sequencies, support=1):

    #print(check_sequence)
    
    first = check_sequence[0]

    is_list = isinstance(first, list)

    current_support = 0

    if not is_list:
        #print("TEST1")
        for sequence in sequences:
            for sequence_elements in sequence:
                if sequence_elements == check_sequence:
                    current_support += 1
                    break
    else:
        #print("TEST2")
        first = first[0]
        second = check_sequence[1][0]

        for sequence in sequences:
            sequence_length = len(sequence)
            index = 0
            for sequence_elements in sequence:
                if first in sequence_elements and index < sequence_length-1:
                    next_elem = sequence[index + 1]
                    #print(next_elem)
                    if second in next_elem:
                        current_support += 1
                index += 1
    #print(current_support)
    return current_support >= support


def to_string(sequences):
    string = ""
    if isinstance(sequences[0], list):
        for sequence in sequences:
            string += "( "
            for sequence_elements in sequence:
                string += sequence_elements
            string += " )"
    else:
        string = ',' . join(sequences)
        string = "( " + string + " )"
    return string


def to_key(sequences):
    string = ""
    if isinstance(sequences[0], list):
        for sequence in sequences:
            string += ""
            for sequence_elements in sequence:
                string += sequence_elements
            string += ""
    else:
        string = '_'.join(sequences)
        string = "" + string + ""
    return string



s1 = [["1", "2"], ["3"], ["1"]]
s2 = [["1", "2"], ["4"]]
s3 = [["1"], ["3", "4"]]
s4 = [["1", "3"], ["5"]]
s5 = [["2"], ["3", "4"]]
s6 = [["2"], ["3", "5"]]

#sequence = s1 + s2 + s3 + s4 + s5 + s6
sequences = []

sequences.append(s1)
sequences.append(s2)
sequences.append(s3)
sequences.append(s4)
sequences.append(s5)
sequences.append(s6)

#print(sequences)

items = get_sequence_ellements(sequences)
#items = ['1', '2']
support = calculate_support(items, sequences)
possible = generate_sequence_2(items, sequences)
# s1 = ['3', '4']
# s2 = ['1', '2']
# possible = [s1, s2]
possible_3 = generate_sequence_3(items, possible)

#to_string(['1', '2'])
#to_string(possible[1])

#print(possible_3)
#print(support)


