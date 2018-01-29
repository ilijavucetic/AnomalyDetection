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

    if isinstance(s2_t[0], list) and len(s2_t[0]) == 1:

        s1_last = s1_t[-1]
        s2_first = s2_t[0]

        if isinstance(s1_last, list) and isinstance(s2_first, list):
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
