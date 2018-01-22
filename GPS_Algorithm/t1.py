
def detectSequence(detect_sequences, sequence, sequence_index):

    for i in range(1, len(detect_sequences)):
        print(sequence_index)

        d_sequence = detect_sequences[i]
        detect_seq_length = len(d_sequence)

        for detect_seq_elem in d_sequence:
            elements_matched = 0
            for j in range(sequence_index, sequence_index+detect_seq_length):

                seq_exists = detect_seq_elem in sequence[j]
                if seq_exists:
                    elements_matched += 1
            part_matched = elements_matched == detect_seq_length
            #print(part_matched)

            return part_matched

sequences = []

s1 = [["1", "2"],["1"],["1", "2"], ["3"],['6'], ['7', '8'],
      ["1", "2"], ["4"], ["1"], ["3", "4"], ["2"], ["3", "4"], ["2"], ["3", "5"]]
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

sequence = sequences[0]
detect_sequence = s3[0]

print(sequence)
print(detect_sequence)

detect_sequence_length = len(detect_sequence)

is_detected = False
part_matched = False

index = 0

for detect_seq in detect_sequence:
    detect_seq_length = len(detect_seq)

    if is_detected:
        break

    for detect_seq_elem in detect_seq:
        elements_matched = 0
        seq_index = 0

        sequences_length = len(sequence)
        for seq in sequence:
            for seq_elem in seq:
                seq_exists = detect_seq_elem in seq_elem
                if seq_exists:
                    elements_matched += 1
            part_matched = elements_matched == detect_seq_length
            print(index)
            if part_matched and index <= detect_seq_length-1 and seq_index <= sequences_length - detect_seq_length - 1:

                matched = detectSequence(detect_sequence, sequence, seq_index+1)

                if matched:
                    is_detected = True
                    break
            seq_index += 1
    index += 1


