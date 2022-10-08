import numpy as np


# file = open("Day5InputPart1", "r")

# if file.mode == "r":
#    content = file.read()
#    intCode = list(map(int, content.split(",")))


def getParametesAndOpCode(list, indexTracker):
    paramAndOpCode = [0, 0, 0, 0, 0]
    count = -1
    for char in str(list[indexTracker])[::-1]:
        paramAndOpCode[count] = int(char)
        count -= 1
    if paramAndOpCode[3] == 0:
        paramAndOpCode[3] = paramAndOpCode[4]
    else:
        paramAndOpCode[3] = int(str(str(paramAndOpCode[3]) + str(paramAndOpCode[4])))
    return paramAndOpCode[:4]


def op1AddFunction(codeInts, parameters, indexTracker, relativeBase):
    if parameters[-1] == 1:
        print("Error, this should not happen")
        return

    values = []
    for param in parameters[:-1]:
        if param == 0:
            values.append(codeInts[codeInts[indexTracker]])
        elif param == 1:
            values.append(codeInts[indexTracker])
        elif param == 2:
            values.append(codeInts[(codeInts[indexTracker] + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    if parameters[-1] == 2:
        codeInts[codeInts[indexTracker] + relativeBase] = sum(values)
    else:
        codeInts[codeInts[indexTracker]] = sum(values)


def op2MultFunction(codeInts: list, parameters, indexTracker, relativeBase):
    if parameters[-1] == 1:
        print("Error, this should not happen1")
        return

    values = []
    for param in parameters[:-1]:
        if param == 0:
            values.append(codeInts[codeInts[indexTracker]])
        elif param == 1:
            values.append(codeInts[indexTracker])
        elif param == 2:
            values.append(codeInts[(codeInts[indexTracker] + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    if parameters[-1] == 2:
        codeInts[codeInts[indexTracker] + relativeBase] = np.prod(values)
    else:
        codeInts[codeInts[indexTracker]] = np.prod(values)


def op3(codeInts, params, indexTracker: int, inputs: list, relativeBase):
    if not inputs:
        inputValue = input("Enter input value: ")
    else:
        inputValue = inputs[0]
        del inputs[0]
    if params[0] == 0:
        codeInts[codeInts[indexTracker]] = int(inputValue)
    elif params[0] == 1:
        codeInts[indexTracker] = int(inputValue)
    elif params[0] == 2:
        codeInts[codeInts[indexTracker] + relativeBase] = int(inputValue)


def op4(codeInts, parameters, indexTracker, relativeBase):
    values = []
    for param in parameters[:-2]:
        if param == 0:
            values.append(codeInts[codeInts[indexTracker]])
        elif param == 1:
            values.append(codeInts[indexTracker])
        elif param == 2:
            values.append(codeInts[(codeInts[indexTracker] + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    print("opCode 4: Here is the output: " + str(values[0]) + " and IndexTracker: " + str(indexTracker))
    return values[0]


def op5(codeInts, parameters, indexTracker, relativeBase):
    originalIndexTracker = indexTracker
    values = []
    for param in parameters[:-1]:
        valueAtIndex = codeInts[indexTracker]
        if param == 0:
            values.append(codeInts[valueAtIndex])
        elif param == 1:
            values.append(valueAtIndex)
        elif param == 2:
            values.append(codeInts[(valueAtIndex + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    if values[0] != 0:
        return values[1]
    else:
        return originalIndexTracker + 2


def op6(codeInts, parameters, indexTracker, relativeBase):
    originalIndexTracker = indexTracker
    values = []
    for param in parameters[:-1]:
        valueAtIndex = codeInts[indexTracker]
        if param == 0:
            values.append(codeInts[valueAtIndex])
        elif param == 1:
            values.append(valueAtIndex)
        elif param == 2:
            values.append(codeInts[(codeInts[indexTracker] + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    if values[0] == 0:
        return values[1]
    else:
        return originalIndexTracker + 2


def op7(codeInts, parameters, indexTracker, relativeBase):
    values = []
    for param in parameters[:-1]:
        valueAtIndex = codeInts[indexTracker]
        if param == 0:
            values.append(codeInts[valueAtIndex])
        elif param == 1:
            values.append(valueAtIndex)
        elif param == 2:
            values.append(codeInts[(valueAtIndex + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    if values[0] < values[1]:
        if parameters[-1] == 2:
            codeInts[codeInts[indexTracker] + relativeBase] = 1
        else:
            codeInts[codeInts[indexTracker]] = 1
    else:
        if parameters[-1] == 2:
            codeInts[codeInts[indexTracker] + relativeBase] = 0
        else:
            codeInts[codeInts[indexTracker]] = 0


def op8(codeInts, parameters, indexTracker, relativeBase):
    values = []
    for param in parameters[:-1]:
        valueAtIndex = codeInts[indexTracker]
        if param == 0:
            values.append(codeInts[valueAtIndex])
        elif param == 1:
            values.append(valueAtIndex)
        elif param == 2:
            values.append(codeInts[(codeInts[indexTracker] + relativeBase)])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    if values[0] == values[1]:
        if parameters[-1] == 2:
            codeInts[codeInts[indexTracker] + relativeBase] = 1
        else:
            codeInts[codeInts[indexTracker]] = 1
    else:
        if parameters[-1] == 2:
            codeInts[codeInts[indexTracker] + relativeBase] = 0
        else:
            codeInts[codeInts[indexTracker]] = 0


def op9AdjustRelativeBase(codeInts, parameters, indexTracker, relativeBase):
    values = []
    for param in parameters[:-1]:
        if param == 0:
            values.append(codeInts[codeInts[indexTracker]])
        elif param == 1:
            values.append(codeInts[indexTracker])
        elif param == 2:
            a = codeInts[indexTracker]
            b = codeInts[codeInts[indexTracker] + relativeBase]
            values.append(codeInts[codeInts[indexTracker] + relativeBase])
        else:
            print("Error, this should not happen")
        indexTracker += 1
    return values[0]


def readIntCode(intCtemp: list, inputs: list, indexTracker: int):
    indexTracker = indexTracker
    latestOutput = 0
    relBase = 0
    intC = np.pad(intCtemp, [0, 100000], 'constant')

    while True:
        parametersAndOpCode = getParametesAndOpCode(intC, indexTracker)
        parameters = parametersAndOpCode[:3][::-1]
        opCode = parametersAndOpCode[-1]

        indexTracker += 1  # Moving forward one step because opCode retrieved

        if opCode == 1:
            op1AddFunction(intC, parameters, indexTracker, relBase)
            indexTracker += 3
        elif opCode == 2:
            op2MultFunction(intC, parameters, indexTracker, relBase)
            indexTracker += 3
        elif opCode == 3:
            op3(intC, parameters, indexTracker, inputs, relBase)
            indexTracker += 1
        elif opCode == 4:
            latestOutput = op4(intC, parameters, indexTracker, relBase)
            indexTracker += 1
            # return [intC, opCode, latestOutput, indexTracker]
        elif opCode == 5:
            indexTracker = op5(intC, parameters, indexTracker, relBase)
        elif opCode == 6:
            indexTracker = op6(intC, parameters, indexTracker, relBase)
        elif opCode == 7:
            op7(intC, parameters, indexTracker, relBase)
            indexTracker += 3
        elif opCode == 8:
            op8(intC, parameters, indexTracker, relBase)
            indexTracker += 3
        elif opCode == 9:
            relBase += op9AdjustRelativeBase(intC, parameters, indexTracker, relBase)
            indexTracker += 1
        elif opCode == 99:
            return [intC, opCode, latestOutput, indexTracker]  # Returns the latest output here
        elif indexTracker + 1 > len(intC):
            print("Out of list range, this should not occur (opCode 99 should have happened).")
            break
        if latestOutput > 10E12:
            print("The thrusters explodes with this")
            break


# print(readIntCode([3,9,8,9,10,9,4,9,99,-1,8]))
# readIntCode(intCode, None)
# print(list)

file = open("Day9input", "r")
content = file.read()
aba = list(map(int, content.split(",")))

readIntCode(aba[:], [], 0)
