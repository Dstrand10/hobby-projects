def isDuoDigit(number: int):
    return len(set(str(number))) <= 2


duodigitMemory = {}
smallestDuoDigitMultiple = []


def checkMemory(nbr):
    for mem in duodigitMemory:
        value = duodigitMemory[mem]
        if mem != 0 and mem % nbr == 0 and value % nbr == 0:
            return value


for nbr in range(5000):
    multiple = 1
    visitedNumbers = []
    print("Doing number: " + str(nbr))
    while True:
        #visitedNumbers.append(nbr * multiple)

        if isDuoDigit(nbr * multiple):
            print("Found smallest duoDigit by logic: " + str(nbr * multiple))
            #for visitedNbr in visitedNumbers:
            #    duodigitMemory[visitedNbr] = nbr * multiple
            smallestDuoDigitMultiple.append(nbr * multiple)
            break
        #duoDigitFromMemory = checkMemory(nbr * multiple)
        #if isinstance(duoDigitFromMemory, int):
        #    print("Found smallest duoDigit by memory: " + str(duoDigitFromMemory))
        #    for visitedNbr in visitedNumbers:
        #        duodigitMemory[visitedNbr] = duoDigitFromMemory
        #    smallestDuoDigitMultiple.append(duoDigitFromMemory)
        #    break
        multiple += 1
print(duodigitMemory)
print(sum(smallestDuoDigitMultiple))
