
with open("input.txt") as f:
    totPaper = 0
    totRibbon = 0
    for line in f.readlines():
        lengths = list(map(int, line.replace("\n", "").split("x")))
        lengths.sort()
        totPaper += 3 * lengths[0] * lengths[1] + 2 * lengths[0] * lengths[2] + 2 * lengths[1] * lengths[2]
        totRibbon += 2 * lengths[0] + 2 * lengths[1] + lengths[0] * lengths[1] * lengths[2]
    print("Answer 1: " + str(totPaper))
    print("Answer 2: " + str(totRibbon))