import copy
#array = [3, [1, 3]]

#sorted(array)
# s1 = [['3'], ['1']]
# s2 = [['1', '3']]

s1 = [['1', '2'], ['4']]
s2 = [['2'], ['3', '4']]

#[['3'], ['1', ['1', '3']]]


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
        print("MERGE")
        merged = []

        if isinstance(s1_last, list):
            print("LIST")
            for temp12 in s2_last:
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
    return s3


print(s1)
print(s2)
s3 = get_new_sequence(s1, s2)
print(s3)
