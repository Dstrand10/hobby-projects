
def calcNextNumber(number):
    oldList = list(str(number))
    newList = ''
    idx = 0
    cnt = 0
    lastNbr = oldList[0]
    while idx < len(oldList):
        currNbr = oldList[idx]
        if currNbr != lastNbr:
            newList += str(cnt)
            newList += str(lastNbr)
            cnt = 1
        else:
            cnt += 1
        lastNbr = currNbr
        idx += 1
    newList += str(cnt)
    newList += str(lastNbr)
    return int(newList)

numberToProcess = 1113222113
for i in range(40):
    numberToProcess = calcNextNumber(numberToProcess)
print("answer 1: " + str(len(str(numberToProcess))))

# Takes at least 10 min
for i in range(10):
    numberToProcess = calcNextNumber(numberToProcess)
print("answer 2: " + str(len(str(numberToProcess))))
