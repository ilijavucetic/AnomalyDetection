import copy


class GspAlgorithm:

    current_sequence_length = 0
    items = []
    all_items = []
    items_support = {}

    def __init__(self, data_set):
        self.data_set = data_set
        self.gsp_algorithm(4)

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

        self.all_items.append(self.items)

    def gsp_algorithm(self, k):

        for length in range(1, k + 1):
            self.generate_sequence(length)

    def generate_sequence(self, length):

        if length == 1:
            print('Generate sequence length', length)
            self.get_sequence_single_elements()
            self.increment_sequence_length()
            print(self.all_items)
            pass
        elif length == 2:
            print('Generate sequence length', length)
            self.get_sequence_2()
            self.increment_sequence_length()
            print('Calculate support', length)
            print(self.all_items)
            pass
        else:
            print('Generate sequence length', length)
            print('Calculate support', length)
            self.generate_sequence_3_plus(length)
            pass
        pass

    def get_sequence_2(self):
        possible_sequences = []
        items = self.items

        for item_first in items:
            for item_second in items:
                if item_first == item_second:

                    pattern = [[item_first], [item_second]]
                    support = self.check_support(pattern)
                    if support:
                        possible_sequences.append(pattern)
                        key = self.to_string(pattern)
                        self.items_support[key] = support
                else:
                    pattern1 = [[item_first], [item_second]]
                    pattern2 = [item_first, item_second]

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

    def calculate_support(self):

        detect_sequences = self.all_items[self.current_sequence_length]

        for detect_sequence in detect_sequences:
            for sequence in self.data_set:
                self.detect_sequence(detect_sequence, sequence)
        pass

    def detect_sequence(self, find_sequence, in_sequence):

        # if find_sequence == [["1"], ["3", "4"]]:
        #     pass
        # else:
        #     return False
        # print("find_sequence", find_sequence)
        # print("in_sequence", in_sequence)

        detect_sequence_length = len(find_sequence)

        is_detected = False
        part_matched = False

        is_detected = False
        part_matched = False

        index = 0

        detect_first_ellement = find_sequence[0]
        detect_seq_length = len(detect_first_ellement)

        seq_index = 0
        for sequence in in_sequence:
            #print("sequence", sequence)
            elements_matched = 0
            sequences_length = len(sequence)
            #print(detect_first_ellement)
            for detect_me in detect_first_ellement:
                #print("detect_me", detect_first_ellement)
                seq_exists = detect_me in sequence
                if seq_exists:
                    elements_matched += 1
                #print(seq_exists)
            part_matched = elements_matched == detect_seq_length

            # print("len", len(in_sequence))
            # print("seq_index", seq_index)
            # print("detect_sequence_length", detect_sequence_length)
            # print("part_matched", part_matched)
            # print("part_matched", part_matched)
            if part_matched and len(in_sequence) >= seq_index + detect_sequence_length:
                matched = self.detect_rest_sequence(find_sequence, in_sequence, seq_index)
                if matched:
                    is_detected = True
                    break

            seq_index += 1
            #print(part_matched)

        #print(is_detected)
        return is_detected
        #exit()

    def detect_rest_sequence(self, d1, s1, sequence_index):

        # print("DETECT REST")
        # print("find me ", d1)
        # print("here  ", s1)
        # print("at index   ", sequence_index)

        detect_sequences = copy.deepcopy(d1)
        sequence = copy.deepcopy(s1)
        #
        # print("sequence", sequence)
        # print("detect_sequences", detect_sequences)
        # print("sequence_index", sequence_index)
        #
        all_matched = 1

        for i in range(1, len(detect_sequences)):

            if sequence_index + i > len(sequence)-1:
                #print("FAAAAAAAAAK")
                return False

            #print("SLEDECI JE : ", sequence_index + i)

            d_sequence = detect_sequences[i]
            detect_seq_length = len(d_sequence)

            elements_matched = 0
            for detect_seq_elem in d_sequence:
                seq_exists = detect_seq_elem in sequence[sequence_index + i]
                if seq_exists:
                    elements_matched += 1
            part_matched = elements_matched == detect_seq_length
            if part_matched:
                all_matched += 1

        return all_matched == len(detect_sequences)

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

    def generate_sequence_3_plus(self, length=3):

        generated_sequence = []
        cross_table = {}

        sequences_2 = self.all_items[self.current_sequence_length-1]

        for sequence in sequences_2:

            sequence_length = len(sequence)

            first = sequence[0]
            last = sequence[sequence_length-1]

            sequence_key = self.to_string(sequence)
            #print("sequence_key", sequence_key)
            cross_table[sequence_key] = {}
            cross_table[sequence_key]["minus_first"] = []
            cross_table[sequence_key]["minus_last"] = []

            single_mesure = True
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
                    temp_array.pop(0)
                    if len(temp_array) == 1:
                        temp_array = temp_array[0]

                    cross_table[sequence_key]["minus_first"].append(temp_array)
                    pass

                if len(last) > 1:
                    temp_array = []
                    for i in range(0, len(last)):
                        temp_array = copy.deepcopy(last)
                        temp_array.remove(last[i])

                        first_temp = []

                        for j in range(0, sequence_length-1):
                            first_temp.append(sequence[j])

                        first_temp.append(temp_array)
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
            key = self.to_string(sequence)

            sequence_minus_first = cross_table[key]["minus_first"]

            for sequence_other in sequences_2:
                lenth_other = len(sequence_other)
                key_other = self.to_string(sequence_other)

                if key != key_other:

                    sequence_other_minus_last = cross_table[key_other]["minus_last"]
                    break_outer = False
                    for first in sequence_minus_first:
                        if break_outer:
                            break

                        for last in sequence_other_minus_last:

                            # TODO CHECK
                            # first = sorted(first)
                            # last = sorted(last)

                            if first == last:
                                temp = self.get_new_sequence(sequence, sequence_other)
                                # print("1", sequence)
                                # print("2", sequence_other)
                                # print("sum : ", temp)
                                if temp not in generated_sequence:
                                    generated_sequence.append(temp)

                                break_outer = True
                                break

        print("generated_sequence", generated_sequence)

        new_array = []
        for detect_me in generated_sequence:
            for sequence in self.data_set:

                detected = self.detect_sequence(detect_me, sequence)
                if detected:
                    new_array.append(detect_me)
                    # print("Detect seq",  detect_me)
                    # print("Detect in ", sequence)
                    # print(detected)

        self.all_items.append(new_array)
        self.current_sequence_length += 1

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

    @staticmethod
    def get_new_sequence(s1, s2):

        s1_t = copy.deepcopy(s1)
        s2_t = copy.deepcopy(s2)
        s1_length = len(s1_t)

        s3 = []

        s1_last = s1_t[-1]
        s2_last = s2_t[-1]

        # SEPERATE ELLEMNT
        if isinstance(s2_last, list) and len(s2_last) == 1:
            if isinstance(s1_last, list):
                for elem in s1_t:
                    s3.append(elem)
                s3.append(s2_last)
            else:
                s3 = [s1, s2_last]
        # MERGE
        else:

            merged = []
            # Case 1 : Not Single mesure
            if isinstance(s2_last, list):
                for temp12 in s2_last:
                    if temp12 not in merged:
                        merged.append(temp12)

                for t in s1_t[:-1]:
                    s3.append(t)
                s3.append(merged)
            else:
                #print("MERGED Single")

                if isinstance(s1_last, list):
                    for temp12 in s2_t:
                        if temp12 not in merged:
                            merged.append(temp12)

                    for t in s1_t[:-1]:
                        s3.append(t)
                    s3.append(merged)
                else:
                    new_elem = []
                    for elem in s2_t:
                        if elem not in s1_t:
                            new_elem.append(elem)
                    s3 = s1_t + new_elem

            # if isinstance(s1_last, list):
            #     for temp12 in s2_t:
            #         if temp12 not in merged:
            #             merged.append(temp12)
            #
            #     for t in s1_t[:-1]:
            #         s3.append(t)
            #     s3.append(merged)
            # else:
            #     new_elem = []
            #     for elem in s2_t:
            #         if elem not in s1_t:
            #             new_elem.append(elem)
            #     s3 = s1_t + new_elem
        return s3

    @staticmethod
    def get_new_sequence2(s1, s2):

        s1_t = copy.deepcopy(s1)
        s2_t = copy.deepcopy(s2)
        s3 = []
        if isinstance(s2_t[len(s2_t) - 1], list) and len(s2_t[len(s2_t) - 1]) == 1:

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
                # temp = s2_t[1:]
                # s3 = s1_t + temp
                new_elem = []
                for elem in s2_t:
                    if elem not in s1_t:
                        new_elem.append(elem)
                s3 = s1_t + new_elem

        return s3

    @staticmethod
    def increment_sequence_length():
        GspAlgorithm.current_sequence_length += 1


if __name__ == "__main__":
    sequences = []

    s1 = [["1", "2"], ["3"], ["1"]]
    s2 = [["1", "2"], ["4"]]
    s3 = [["1"], ["3", "4"]]
    s4 = [["1", "3"], ["5"]]
    s5 = [["2"], ["3", "4"]]
    s6 = [["2"], ["3", "5"]]
    s7 = [["2"], ["3"], ["5"]]

    sequences.append(s1)
    sequences.append(s2)
    sequences.append(s3)
    sequences.append(s4)
    sequences.append(s5)
    sequences.append(s6)
    sequences.append(s7)

    result = GspAlgorithm(sequences)
    all_items = result.all_items

    # for sequence in all_items:
    #     print("Seq", sequence)
    #     for sequence_elem in sequence:
    #         print(sequence_elem)
    #     pass


    print(result.all_items[-1])