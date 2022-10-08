file = open("Day4InputPart1", "r")

if file.mode == "r":
    content = file.read().split("-")
    lowerLimit = int(content[0])
    upperLimit = int(content[1])


def isCodeNotDecreasing(possibleCode):
    codeAsString = str(possibleCode)
    for count in range(0, len(codeAsString) - 1):
        if int(codeAsString[count + 1]) - int(codeAsString[count]) < 0:
            return False
    return True


def hasCodeTwoAdjacentNumbers(possibleCode):
    codeAsString = str(possibleCode)
    for count in range(0, len(codeAsString) - 1):
        if int(codeAsString[count + 1]) - int(codeAsString[count]) == 0:
            return True
    return False


def hasExactlyTwoAdjacentNumbers(possibleCode):
    codeAsString = str(possibleCode)
    count = 0
    checkForward = 1
    countNumberOfSameNumbers = 1
    hasExactlyTwoAdjacentNumbers = False
    while count + checkForward < len(codeAsString):
        while count + checkForward < len(codeAsString) and int(codeAsString[count + checkForward]) - int(codeAsString[count]) == 0:
            countNumberOfSameNumbers += 1
            checkForward += 1
            if countNumberOfSameNumbers == 2:
                hasExactlyTwoAdjacentNumbers = True
            if countNumberOfSameNumbers > 2:
                hasExactlyTwoAdjacentNumbers = False
        if hasExactlyTwoAdjacentNumbers:
            return True
        count += checkForward
        checkForward = 1
        countNumberOfSameNumbers = 1
    return False


testCode = 111144
print(isCodeNotDecreasing(testCode) and hasCodeTwoAdjacentNumbers(testCode))
print(isCodeNotDecreasing(testCode) and hasExactlyTwoAdjacentNumbers(testCode))


countWorkingCodesPart1 = 0
countWorkingCodesPart2 = 0
for possibleCode in range(lowerLimit, upperLimit + 1):
    if isCodeNotDecreasing(possibleCode) and hasCodeTwoAdjacentNumbers(possibleCode):
        countWorkingCodesPart1 += 1
    if isCodeNotDecreasing(possibleCode) and hasExactlyTwoAdjacentNumbers(possibleCode):
        countWorkingCodesPart2 += 1

print(countWorkingCodesPart1)
print(countWorkingCodesPart2)

