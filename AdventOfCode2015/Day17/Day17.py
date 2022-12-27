import itertools as it

with open("input.txt") as f:
    jars = list(map(lambda x: int(x.replace("\n", "")), f.readlines()))
    totalCombinations = 0
    for i in range(len(jars)):
        totalCombinations += len(list(filter(lambda x: sum(x) == 150, it.combinations(jars, i + 1))))
    print("Answer 1: " + str(totalCombinations))
    totalCombinations = 0
    for i in range(len(jars)):
        totalCombinations += len(list(filter(lambda x: sum(x) == 150, it.combinations(jars, i + 1))))
        if totalCombinations > 0:
            break
    print("Answer 2: " + str(totalCombinations))
