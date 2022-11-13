import itertools

def calculateOptimalHappiness(persons, happiness):
    optimalHappiness = 0
    for perm in itertools.permutations(persons, len(persons)):
        currentHappiness = 0
        for idx, person in enumerate(perm):
            if idx - 1 < 0:
                leftPersonIdx = -1
            else:
                leftPersonIdx = idx - 1
            if idx + 1 >= len(persons):
                rightPersonIdx = 0
            else:
                rightPersonIdx = idx + 1
            currentHappiness += happiness[(person, perm[leftPersonIdx])]
            currentHappiness += happiness[(person, perm[rightPersonIdx])]
        if currentHappiness > optimalHappiness:
            optimalHappiness = currentHappiness
    return optimalHappiness


with open("input.txt") as f:
    #Data cleaning
    data = f.readlines()
    happiness = dict()
    persons = set()
    for datarow in data:
        firstName = datarow.split(" would ")[0]
        secondName = datarow.split(" to ")[-1].replace(".", "").replace("\n", "")
        points = int(datarow.split(" ")[3])
        if datarow.split(" ")[2] == "gain":
            happiness[(firstName, secondName)] = points
        else:
            happiness[(firstName, secondName)] = -points
        persons.add(firstName)
    persons = list(persons)

    #Part 1
    print("Answer 1: " + str(calculateOptimalHappiness(persons, happiness)))

    #Part 2
    for person in persons:
        happiness[('Daniel', person)] = 0
        happiness[(person, 'Daniel')] = 0
    persons.append('Daniel')
    print("Answer 2: " + str(calculateOptimalHappiness(persons, happiness)))