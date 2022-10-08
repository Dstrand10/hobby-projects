def isNice(line):
    vowels = "aeiou"
    nbrOfVowels = 0
    twoSubsequentletters = False
    twoCharCombos = list(zip(line[:-1], line[1:]))
    for charCombo in twoCharCombos:
        if charCombo in [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]:
            return False
        if charCombo[0] in vowels:
            nbrOfVowels += 1
        if charCombo[0] == charCombo[1]:
            twoSubsequentletters = True
    if twoCharCombos[-1][1] in vowels:
        nbrOfVowels += 1
    return nbrOfVowels >= 3 and twoSubsequentletters


def isNice2(line):
    doubleCharInterval = False
    sameCharsOneBetween = False
    twoCharCombos = list(zip(line[:-1], line[1:]))
    for idx, twoCharCombo in enumerate(twoCharCombos):
        if idx < len(twoCharCombos) - 2 and twoCharCombo in twoCharCombos[idx + 2:]:
            doubleCharInterval = True
        if idx < len(twoCharCombos) - 1:
            if twoCharCombo[0] == twoCharCombos[idx+1][1]:
                sameCharsOneBetween = True
    #return doubleCharInterval
    #return sameCharsOneBetween

    return doubleCharInterval and sameCharsOneBetween

with open("input.txt") as f:
    totNiceStrings = 0
    lines = f.readlines()
    for line in lines:
        if isNice(line.replace("\n", "")):
            totNiceStrings += 1
    print("Answer 1: " + str(totNiceStrings))

    totNiceStrings2 = 0
    for line in lines:
        if isNice2(line.replace("\n", "")):
            print(line)
            totNiceStrings2 += 1
    print(totNiceStrings2)