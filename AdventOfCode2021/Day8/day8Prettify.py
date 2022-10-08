def checkNumbers(nbrs_contained, chars, pos_nbrs):
    for nbr_con in nbrs_contained:
        for char in nbr_con:
            for pos_nbr in pos_nbrs:
                if char not in pos_nbr:
                    pos_nbrs.remove(pos_nbr)
    for char in chars:
        for pos_nbr in pos_nbrs:
            if char not in pos_nbr:
                pos_nbrs.remove(pos_nbr)

    return pos_nbrs


with open("input.txt") as f:
    input_data = [x.split(" | ") for x in f.read().split("\n")]

    ans = 0
    for row in input_data:
        output = row[1].split(" ")

        for output_nbr in output:
            if len(output_nbr) in [2, 3, 4, 7]:
                ans += 1

    print("Solution 1: " + str(ans))

    tot = 0
    for row in input_data:
        nbrs = {}
        input_row = [''.join(sorted(x)) for x in row[0].split(" ")]
        nbrs[1] = next((nbr for nbr in input_row if len(nbr) == 2), None)
        nbrs[4] = next((nbr for nbr in input_row if len(nbr) == 4), None)
        nbrs[7] = next((nbr for nbr in input_row if len(nbr) == 3), None)
        nbrs[8] = next((nbr for nbr in input_row if len(nbr) == 7), None)
        pos_2_3 = nbrs[7].translate({ord(c): None for c in nbrs[1]})
        nbrs[9] = checkNumbers([nbrs[1], nbrs[4], nbrs[7]], [pos_2_3],
                               [nbr for nbr in input_row if len(nbr) == 6 and nbr not in list(nbrs.values())])[0]
        pos_1_1 = nbrs[8].translate({ord(c): None for c in nbrs[9]})
        nbrs[0] = checkNumbers([nbrs[1], nbrs[7]], [pos_2_3, pos_1_1],
                               [nbr for nbr in input_row if len(nbr) == 6 and nbr not in list(nbrs.values())])[0]
        pos_2_2 = nbrs[8].translate({ord(c): None for c in nbrs[0]})
        nbrs[6] = checkNumbers([], [pos_2_3, pos_1_1, pos_2_2],
                               [nbr for nbr in input_row if len(nbr) == 6 and nbr not in list(nbrs.values())])[0]
        pos_3_2 = nbrs[8].translate({ord(c): None for c in nbrs[6]})
        pos_3_1 = nbrs[1].replace(pos_3_2, '')
        nbrs[3] = checkNumbers([nbrs[1], nbrs[7]], [pos_2_3, pos_2_2, pos_3_2, pos_3_1],
                               [nbr for nbr in input_row if len(nbr) == 5 and nbr not in list(nbrs.values())])[0]
        pos_1_2 = nbrs[4].translate({ord(c): None for c in nbrs[3]})
        nbrs[5] = checkNumbers([], [pos_2_2, pos_1_2, pos_2_3, pos_3_1],
                               [nbr for nbr in input_row if len(nbr) == 5 and nbr not in list(nbrs.values())])[0]
        nbrs[2] = checkNumbers([], [],
                               [nbr for nbr in input_row if len(nbr) == 5 and nbr not in list(nbrs.values())])[0]

        output_row = [''.join(sorted(x)) for x in row[1].split(" ")]
        ans = []
        for out_nbr in output_row:
            ans.append(str(list(nbrs.keys())[list(nbrs.values()).index(out_nbr)]))
        tot += int(''.join(ans))

    print("Solution 2: " + str(tot))