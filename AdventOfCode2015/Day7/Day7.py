def getDigitFromWireOrNumber(fromWiresOrNumber):
    if fromWiresOrNumber.isdigit():
        return int(fromWiresOrNumber)
    else:
        return int(wires[fromWiresOrNumber])


def checkWireSignalsExist(wires, fromWiresOrNumber):
    for wireOrNumber in fromWiresOrNumber:
        if wireOrNumber is not None and not wireOrNumber.isdigit() and wireOrNumber not in wires.keys():
            return False
    return True


def updateWires(wires, commands):
    idx = 0
    while len(commands) > 0:
        operator = commands[idx][0]
        fromWiresOrNumber = commands[idx][1]
        toWire = commands[idx][2]

        if not checkWireSignalsExist(wires, fromWiresOrNumber):
            idx = (idx + 1) % len(commands)
            continue

        if operator == '':
            wires[toWire] = getDigitFromWireOrNumber(fromWiresOrNumber[0])

        elif operator == "NOT":
            wires[toWire] = ~getDigitFromWireOrNumber(fromWiresOrNumber[0]) & 65535

        elif operator == "AND":
            wires[toWire] = getDigitFromWireOrNumber(fromWiresOrNumber[0]) & getDigitFromWireOrNumber(
                fromWiresOrNumber[1])

        elif operator == "OR":
            wires[toWire] = getDigitFromWireOrNumber(fromWiresOrNumber[0]) | getDigitFromWireOrNumber(
                fromWiresOrNumber[1])

        elif operator == "LSHIFT":
            wires[toWire] = getDigitFromWireOrNumber(fromWiresOrNumber[0]) << getDigitFromWireOrNumber(
                fromWiresOrNumber[1])

        elif operator == "RSHIFT":
            wires[toWire] = getDigitFromWireOrNumber(fromWiresOrNumber[0]) >> getDigitFromWireOrNumber(
                fromWiresOrNumber[1])

        else:
            EOFError

        commands.remove(commands[idx])
        idx = 0
    return wires


def updateWiresPreface(wires, commands, startValues):
    if startValues is not None:
        for (wire, value) in startValues:
            commands = list(filter(lambda command: command[-1] != wire, commands))
            wires[wire] = value
        return updateWires(wires, commands)
    else:
        return updateWires(wires, commands)


with open("input.txt") as f:
    commands = []
    for line in f.readlines():
        tmp_line = line.replace("\n", "").split(" ")
        if tmp_line[0] == "NOT":
            commands.append((
                "NOT",  # command
                (tmp_line[1], None),  # from wire or number
                tmp_line[-1]  # to_wire
            ))
        elif len(tmp_line) == 3:
            commands.append((
                "",  # command
                (tmp_line[0], None),  # from wire or number
                tmp_line[-1]  # to_wire
            ))
        else:
            commands.append((
                tmp_line[1],  # command
                (tmp_line[0], tmp_line[2]),  # from wires or number
                tmp_line[-1]  # to_wire
            ))

    wires = {}
    updateWiresPreface(wires, commands.copy(), None)
    ans1 = wires['a']
    print("Answer 1: " + str(ans1))
    wires = {}
    updateWiresPreface(wires, commands.copy(), [('b', ans1)])
    ans2 = wires['a']
    print("Answer 2: " + str(ans2))
