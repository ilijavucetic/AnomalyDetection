#from GPS_Algorithm.gsp_algorithm import gsp_algorithm
import copy
sequences = []

s1 = [["1", "2"], ["3"], ["1"]]
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


class GspAlgorithm:

    items = []
    all_items = []
    current_sequence_length = 0
    items_support = {}

    def __init__(self, data_set):
        self.data_set = data_set
        self.get_sequence_single_elements()
        #print(self.items)
        self.gsp_algorithm(3)

    def gsp_algorithm(self, k):

        for length in range(1, k + 1):
            self.generate_sequence(length)
        pass

    def generate_sequence(self, length):

        if length == 1:
            print('Generate sequence length', length)
            self.get_sequence_single_elements()
            self.current_sequence_length += 1
            #self.calculate_support()
            pass
        elif length == 2:
            print('Generate sequence length', length)
            self.get_sequence_2()
            self.current_sequence_length += 1
            print('Calculate support', length)
            pass
        else:
            print('Generate sequence length', length)
            print('Calculate support', length)
            self.generate_sequence_3_plus(length)
            pass
        pass

    def get_sequence_single_elements(self):

        for sequence in sequences:
            for sequence_elements in sequence:
                for element in sequence_elements:
                    if element not in self.items:
                        self.items.append(element)

        for item in self.items:
            self.items_support[item] = 0
            for sequence in sequences:
                for sequence_elements in sequence:
                    if item in sequence_elements:
                        self.items_support[item] += 1
                        break
        #print("SUPPORT", self.items_support)

        self.all_items.append(self.items)

        #return items

    def get_sequence_2(self):
        possible_sequences = []
        items = self.items

        for item_first in items:
            for item_second in items:
                if item_first == item_second:

                    pattern = [[item_first], [item_second]]
                    # print(pattern)
                    # is_valid = check_support(pattern, sequences)
                    support = self.check_support(pattern)
                    if support:
                        possible_sequences.append(pattern)
                        key = self.to_string(pattern)
                        self.items_support[key] = support
                else:
                    pattern1 = [[item_first], [item_second]]
                    pattern2 = [item_first, item_second]
                    # print(pattern1)
                    # print(pattern2)

                    # is_valid_1 = check_support(pattern1, sequences)
                    # is_valid_2 = check_support(pattern2, sequences)
                    #
                    support1 = self.check_support(pattern1)
                    support2 = self.check_support(pattern2)

                    if support1:
                        possible_sequences.append(pattern1)
                        key1 = self.to_string(pattern1)
                        self.items_support[key1] = support1
                    if support2:
                        possible_sequences.append(pattern2)
                        key2 = self.to_string(pattern1)
                        self.items_support[key2] = support2

        self.all_items.append(possible_sequences)
        #print("SUPPORT 2 ", self.items_support)
        #return possible_sequences

    def calculate_support(self):

        detect_sequences = self.all_items[self.current_sequence_length]

        for detect_sequence in detect_sequences:
            print('Detect', detect_sequence)

            for sequence in self.data_set:
                print('Sequence', sequence)

                self.detect_sequence(detect_sequence, sequence)

        #print('Calculate support')
        #print(self.items)
        pass

    def detect_sequence(self, find_sequence, in_sequence):

        sequence = in_sequence
        detect_sequence = find_sequence[0]

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
                    #print(index)
                    if part_matched and index <= detect_seq_length - 1 and seq_index <= sequences_length - detect_seq_length - 1:

                        matched = self.detect_rest_sequence(detect_sequence, sequence, seq_index + 1)

                        if matched:
                            is_detected = True
                            break
                    seq_index += 1
            index += 1

        #print(is_detected)
        return is_detected
        #print(find_sequence, in_sequence)
        #print("IS DETECTED", is_detected)
        pass

    def detect_rest_sequence(self, detect_sequences, sequence, sequence_index):

        for i in range(1, len(detect_sequences)):

            d_sequence = detect_sequences[i]
            detect_seq_length = len(d_sequence)

            for detect_seq_elem in d_sequence:
                elements_matched = 0
                for j in range(sequence_index, sequence_index+detect_seq_length):

                    seq_exists = detect_seq_elem in sequence[j]
                    if seq_exists:
                        elements_matched += 1
                part_matched = elements_matched == detect_seq_length

                return part_matched

    def check_support(self, check_sequence, support=1):

        sequences = self.data_set
        first = check_sequence[0]

        is_list = isinstance(first, list)

        current_support = 0

        if not is_list:
            for sequence in sequences:
                for sequence_elements in sequence:
                    if sequence_elements == check_sequence:
                        current_support += 1
                        break
        else:
            first = first[0]
            second = check_sequence[1][0]

            for sequence in sequences:
                sequence_length = len(sequence)
                index = 0
                for sequence_elements in sequence:
                    if first in sequence_elements and index < sequence_length-1:
                        next_elem = sequence[index + 1]
                        if second in next_elem:
                            current_support += 1
                            break
                    index += 1
        # print("p", check_sequence)
        # print("s", current_support)
        return current_support

    @staticmethod
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

    def generate_sequence_3_plus(self, length=3):

        generated_sequence = []
        cross_table = {}

        sequences_2 = self.all_items[self.current_sequence_length]

        for sequence in sequences_2:

            first = sequence[0]
            #
            sequence_key = self.to_string(sequence)

            cross_table[sequence_key] = {}
            cross_table[sequence_key]["first"] = []
            cross_table[sequence_key]["second"] = []

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

        print(cross_table)


        print(sequences_2)
        #exit()
        for sequence in sequences_2:
            key = self.to_string(sequence)

            #print(key)

            sequence_minus_first = cross_table[key]["first"]
        #
            for sequence_other in sequences_2:
                lenth_other = len(sequence_other)
                #print(sequence_other)
                key_other = self.to_string(sequence_other)
                #print(key_other)
        #
                if key != key_other:

                    print(key_other)
                    print(key_other == "( 1 )( 3145 )")
                    sequence_other_minus_last = cross_table[key_other]["second"]
                    break_outer = False
                    for first in sequence_minus_first:
                        if break_outer:
                            break

                        for last in sequence_other_minus_last:

                            if first == last:
                                # print(sequence)
                                # print(sequence_other)
                                temp = self.get_new_sequence(sequence, sequence_other)
                                # print(temp)

                                # print(key)
                                # print(key_other)
                                # print("sequence", sequence)
                                # print("sequence_other", sequence_other)
                                print(temp)
                                #if key =='( 1,2 )' and key_other == '( 1 )( 3 )':
                                #     print("AAAAA")
                                # #if sequence == [['2'], ['3']]:
                                #     print(key)
                                #     print(key_other)
                                #     print("sequence", sequence)
                                #     print("sequence_other", sequence_other)
                                #     print(temp)
                                #generated_sequence.append(temp)

                                break_outer = True
                                break
        exit()
        #print(generated_sequence)

        # for detect_me in generated_sequence:
        #     #print("Detect me ", detect_me)
        #
        #     for sequence in self.data_set:
        #
        #         detected = self.detect_sequence(detect_me, sequence)
        #         if detected:
        #             print("Detect seq", detect_me)
        #             print("Detect in ", sequence)
        #             print(detected)



        pass

    @staticmethod
    def get_new_sequence(s1, s2):

        s1_t = copy.deepcopy(s1)
        s2_t = copy.deepcopy(s2)
        s3 = []
        if isinstance(s2_t[len(s2_t) - 1], list) and len(s2_t[len(s2_t) - 1]) == 1:
            print("ASDASdasdasdsa")

            s1_last = s1_t[-1]
            s2_first = s2_t[0]

            if isinstance(s1_last, list) and isinstance(s2_first, list):
                temp = s2_t[1:]
                s3 = s1_t + temp
            else:
                s3.append(s1_t)
                temp = s2_t[1:]
                for elem in temp:
                    s3.append(elem)
        else:
            s3 = []
            merged = s1_t[-1]

            if isinstance(merged, list):
                for temp12 in s2_t:
                    if temp12 not in merged:
                        merged.append(temp12)

                for t in s1_t[:-1]:
                    s3.append(t)
                length = len(s3)
                s3.append(merged)
                s3[length] = sorted(s3[length])
            else:
                temp = s2_t[1:]
                s3 = s1_t + temp
                # print("WASD")
                # s3 = [s1]
                # s3 += s2[1:]
        return s3


result = GspAlgorithm(sequences)