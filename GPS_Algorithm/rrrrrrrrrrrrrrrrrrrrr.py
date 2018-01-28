detect_sequences = [['1'], ['3', '4']]
sequence = [['1'], ['3', '4']]

sequence_index = 0

all_matched = 1
for i in range(1, len(detect_sequences)):

    d_sequence = detect_sequences[i]
    detect_seq_length = len(d_sequence)
    print("d_sequence", d_sequence)
    print("d_sequence", detect_seq_length)

    elements_matched = 0
    for detect_seq_elem in d_sequence:
        seq_exists = detect_seq_elem in sequence[sequence_index + i]
        if seq_exists:
            elements_matched += 1
        print(elements_matched)
    part_matched = elements_matched == detect_seq_length
    if part_matched:
        all_matched += 1
print(all_matched == len(detect_sequences))



    # for detect_seq_elem in d_sequence:
    #     elements_matched = 0
    #
    #     print("sequence[sequence_index+i]", sequence[sequence_index+i])
    #     seq_exists = detect_seq_elem in sequence[sequence_index+i]
    #     if seq_exists:
    #         elements_matched += 1
    #     part_matched = elements_matched == detect_seq_length
    #     if part_matched:
    #         all_matched += 1
    #
    # sequence_index += 1

# print("all_matched", all_matched)
# print("LEN:", len(detect_sequences))


