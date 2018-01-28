generated_sequence =\
    [
        [
            ['1'], [['1', '3']]
        ],
        [
            ['1'], ['3']
        ],
        [
            ['1', '3'], ['3']
        ],
        [
            ['1', '3'], ['1']
        ],
        [
            ['2'], [['1', '3']]
        ],
        [
            ['2'], ['3']],
        [
            ['3'], ['1']
        ],
        [
            ['3'], [['1', '3']]
        ]
    ]


data_set =\
    [
        [
            ['1', '2'], ['3'], ['1']
        ],
        [['1', '2'], ['4']], [['1'], ['3', '4']], [['1', '3'], ['5']], [['2'], ['3', '4']],
        [
            ['2'], ['3', '5']
        ]
    ]

for detect_me in generated_sequence:
    for sequence in data_set:
        print("find", detect_me)
        print("in", sequence)

       # detected = detect_sequence(detect_me, sequence)
        #if detected:
            #new_array.append(detect_me)
            # print("Detect seq",  detect_me)
            # print("Detect in ", sequence)
            # print(detected)
        pass