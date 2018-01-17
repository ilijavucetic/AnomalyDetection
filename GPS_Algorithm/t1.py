# array = ['1', '2', '3']
#
# print(array)
#
# array2 = [['4'], ['5']]
#
# temp = array2[1:]
#
# a3 = array + temp
#
# print(a3)
#print(array2[-1])

# a1 = ['1', '2']
# a2 = ['1', '3']
#
# temp = a2[1:]
#
# for elem in temp:
#     a1.append(elem)
#
#
# print(a1)
# #print(a2)


def detectSequence(detect_sequences, sequence, detect_seq_length):
    print(detect_sequences)
    print(sequence)
    print("ALO BRE")
    # detect_seq_length = len(detect_seq)
    # if detect_seq_length > 1:
    #
    #     for detect_seq in detect_sequences:
    #         seq_exists = detect_seq in
    #
    #     pass
    # else:
    #     pass





sequences = []

s1 = [["1", "2"],["1"],["1", "2"], ["3"],['6'], ['7', '8'], ["1", "2"], ["4"], ["1"], ["3", "4"], ["2"], ["3", "4"], ["2"], ["3", "5"]]
s2 = [["1", "2"], ["4"]]
s3 = [["1"], ["3", "4"]]
s4 = [["1", "3"], ["5"]]
s5 = [["2"], ["3", "4"]]
s6 = [["2"], ["3", "5"]]

sequences.append(s1)
sequences.append(s2)
sequences.append(s3)
sequences.append(s4)
sequences.append(s5)
sequences.append(s6)

s3 = [[['1', '2'], ['3']], ['1', '2', '3'], [['1', '2'], ['4']], [['1', '2'], ['5']], [['1', '2'], ['3']], [['1', '2'], ['4']], [['1', '2'], ['5']], [['1'], ['3'], '3'], [[['1'], ['3']], ['1']], [['1'], ['3'], '4'], [[['1'], ['3']], ['5']], [['1'], ['3'], '5'], ['1', '3', '2'], [['1', '3'], ['3']], [['1', '3'], ['4']], [['1', '3'], ['5']], [['1', '3'], ['1']], ['1', '3', '4'], [['1', '3'], ['5']], ['1', '3', '5'], [['1'], ['4'], '4'], [['1'], ['5'], '5'], [['2'], ['3'], '3'], [[['2'], ['3']], ['1']], [['2'], ['3'], '4'], [[['2'], ['3']], ['5']], [['2'], ['3'], '5'], [['2'], ['4'], '4'], [['2'], ['5'], '5'], [['3'], ['1'], '2'], [[['3'], ['1']], ['3']], [['3'], ['1'], '3'], [[['3'], ['1']], ['4']], [[['3'], ['1']], ['5']], ['3', '4', '3'], [['3', '4'], ['1']], [['3', '4'], ['5']], ['3', '4', '5'], [['3'], ['5'], '5'], ['3', '5', '3'], [['3', '5'], ['1']], ['3', '5', '4'], [['3', '5'], ['5']]]

# print(s3[0])
# print(sequences)
# test = s3[0] in sequences
# print(test)

sequence = sequences[0]
detect_sequence = s3[0]

detect_sequence_length = len(detect_sequence)


# print(sequence)
# print(detect_sequence)

is_detected = False
part_matched = False

index = 0

while not is_detected:

    for detect_seq in detect_sequence:
        detect_seq_length = len(detect_seq)

        #check = check_sequence(detect_seq, sequences)
        #print(detect_seq)
        if detect_seq_length > 1:

            for detect_seq_elem in detect_seq:
                #print(detect_seq_elem)
                elements_matched = 0
                seq_index = 0

                sequences_length = len(sequence)
                for seq in sequence:
                    for seq_elem in seq:
                        seq_exists = detect_seq_elem in seq_elem
                        if seq_exists:
                            elements_matched += 1
                    part_matched = elements_matched == detect_seq_length
                    #print(index)
                    #print(index < detect_seq_length-1)
                    #print(seq_index<seq_length-1)
                    #print(part_matched)

                    if part_matched and index < detect_seq_length-1 and seq_index < sequences_length - 1 :

                        detectSequence(detect_sequence[index+1], sequence[seq_index+1], detect_seq_length)
                        # print(index)
                        # print(seq_index)

                    seq_index += 1

                    #print(elements_matched == detect_seq_length)


            # is_part_detected = False
            #
            # while not is_part_detected:
            #
            #     for detect_seq_elem in detect_seq:
            #         for seq in sequence:
            #             seq_exists = detect_seq_elem in seq
            #             print(seq_exists)
            #
            #     break

            pass
        else:
            pass

        index += 1


    break
#
#
#
# temp_sequence = []

# for sequence in sequences:
#     length_sum = 0
#     for sequence_element in sequence:
#         length_sum += len(sequence_element)
#         temp_sequence.append(sequence_element)
#         if length_sum == 3:
#             print(temp_sequence)
#             temp_sequence = []
#             length_sum = 0
#
#
#
#         print(len(sequence_element))
#         print(sequence_element)


# generated_sequence = s3[1]
# sequence_length = len(generated_sequence)
#
# for search_sequence in generated_sequence:
#
#     #if()
#
#     print(isinstance(search_sequence, list))
#     # for sequence in search_sequence:
#     #     print(sequence)


# for generated_sequence in s3[0]:
#
#     for sequence in sequences:
#         sequence_length = len(sequence)
#         index = 0
#         for sequence_element in sequence:
#             if sequence_element == generated_sequence and index < sequence_length-1:
#                 print('detected')
#
#             index += 1
# for sequence in sequences:
#
#     for sequence_element in sequence:
#
#
#
#
#
#             print(generated_sequence)
#
#             # print(s3[0])
#             # print(sequence_element)
#
#
#     # test = s3[0] in sequence
#     # print(s3[0])
#     # print(sequence)
#     # print(test)