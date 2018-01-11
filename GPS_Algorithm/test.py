__author__ = 'Ilija_V_ITS'


# 01,AB(FG)CD
# 02,BGD
# 03,BFG(AB)
# 04,F(AB)CD
# 05,A(BC)GF(DE)

s1 = ["A", "B", ["F", "G"], "C", "D"]
s2 = ["B", "G", "D"]
s3 = ["B", "F", "G", ["A", "B"]]
s4 = ["F", ["A", "B"], "C", "D"]
s5 = ["A", ["B", "C"], "G", "F", ["D", "E"]]

sequences = [s1, s2, s3, s4, s5]

min_support = 2

items = []
items_count = {}

items_2 = []

for sequence in sequences:
    for sequence_element in sequence:
        sequence_length = len(sequence_element)
        if sequence_length > 1:
            for element in sequence_element:
                if element not in items:
                    items.append(element)
                    items_count[element] = 1
                else:
                    items_count[element] += 1
        else:
            if sequence_element not in items:
                items.append(sequence_element)
                items_count[sequence_element] = 1
            else:
                items_count[sequence_element] += 1

        #print(len(sequence_element))
        #print(sequence_element)
#print(items)
#print(items_count)

# for key, value in items_count.items():
#     if value < 2:
#         items.remove(key)

#print(items)

# 1 item sequence
for item_first in items:
    for item_second in items:
        temp_element = item_first + item_second
        for sequence in sequences:
            index = 0
            sequence_length = len(sequence)
            for sequence_element in sequence:

                if len(sequence_element) > 1:
                    for el in sequence_element:
                        if el == item_first and index < sequence_length-1:
                            next_elem = sequence[index+1]

                            if len(next_elem) > 1:
                                for el2 in next_elem:
                                    if el2 == item_second:
                                        #temp_element = item_first + item_second
                                        if temp_element not in items_2:
                                            items_2.append(temp_element)
                                            items_count[temp_element] = 1
                                        else:
                                            items_count[temp_element] += 1
                            else:
                                if next_elem == item_second:
                                    if temp_element not in items_2:
                                        items_2.append(temp_element)
                                        items_count[temp_element] = 1
                                    else:
                                        items_count[temp_element] += 1
                else:
                    if sequence_element == item_first and index < sequence_length-1:
                            next_elem = sequence[index+1]

                            if len(next_elem) > 1:
                                for el2 in next_elem:
                                    if el2 == item_second:
                                        if temp_element not in items_2:
                                            items_2.append(temp_element)
                                            items_count[temp_element] = 1
                                        else:
                                            items_count[temp_element] += 1
                            else:
                                if next_elem == item_second:
                                    if temp_element not in items_2:
                                        items_2.append(temp_element)
                                        items_count[temp_element] = 1
                                    else:
                                        items_count[temp_element] += 1

                # else:
                #
                #
                # if index < sequence_length-1 and sequence_element == item_first and sequence[index+1] == item_second:
                #     #print(item_first + item_second)
                #     temp_element = item_first + item_second
                #     if temp_element not in items_2:
                #         items_2.append(temp_element)
                #         items_count[temp_element] = 1
                #     else:
                #         items_count[temp_element] += 1
                #     #print(sequence[index+1])
                #     pass
                index += 1

        #temp_sequence = item_first + item_second
        #print(item_first + item_second)

# 2 item sequence
for item_first in items:
    for item_second in items:
        if item_first != item_second:
            #print(item_first + item_second)
            temp_element = "(" + item_first + item_second + ")"

            for sequence in sequences:
                #index = 0
                #sequence_length = len(sequence)
                for sequence_element in sequence:
                    if len(sequence_element) > 1:
                        index = 0
                        sequence_length = len(sequence_element)
                        #print(sequence_element)

                        first_matched = False
                        for element in sequence_element:

                            if first_matched:
                                for i in range(index, sequence_length):
                                    #print(i)
                                    if sequence_element[i] == item_second:
                                        if temp_element not in items_2:
                                            items_2.append(temp_element)
                                            items_count[temp_element] = 1
                                        else:
                                            items_count[temp_element] += 1
                                        #break
                                        #print(temp_element)

                            #print(first_matched)
                            if sequence_element[index] == item_first:
                                first_matched = True

                            # if index < sequence_length-1 and sequence_element[index] == item_first and sequence_element[index+1] == item_second:
                            #
                            #     if temp_element not in items_2:
                            #         items_2.append(temp_element)
                            #         items_count[temp_element] = 1
                            #     else:
                            #         items_count[temp_element] += 1

                            index += 1
            pass

items_all = items + items_2

# for key, value in items_count.items():
#     if value < 2:
#         items_all.remove(key)
#
#print(items_all)
#print(items_2)

# 3 items sequence

seq_dict = {}

for sequence in items_2:

    same_sequence = False
    if len(sequence) > 2:
        same_sequence = True
        sequence_r = sequence[1:len(sequence)-1]

        print(sequence_r)
        # for i in range(0, len(sequence_r)):
        #     sequence_r.


    else:
        sequence_r = sequence

    first = sequence_r[0]
    last = sequence_r[len(sequence_r)-1]

    seq_dict[sequence] = [first, last]

    # print(sequence_r)
    # print(first)
    # print(last)

print(seq_dict)




# print(items_2)
# print(items_count)