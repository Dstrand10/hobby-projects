def jump(offset):
    if "+" in offset:
        return int(offset.replace("+", ""))
    else:
        return -int(offset.replace("-", ""))


def runProcess(register):
    pos = 0
    while True:
        if pos >= len(data) or pos < 0:
            break
        instruction = data[pos]
        i = instruction.split(" ")[0]
        if i == "hlf":
            register[instruction.split(" ")[1]] = register[instruction.split(" ")[1]] / 2
            pos += 1
        elif i == "tpl":
            register[instruction.split(" ")[1]] = register[instruction.split(" ")[1]] * 3
            pos += 1
        elif i == "inc":
            register[instruction.split(" ")[1]] = register[instruction.split(" ")[1]] + 1
            pos += 1
        elif i == "jmp":
            pos += jump(instruction.split(" ")[1])
        elif i == "jie":
            if register[instruction.split(" ")[1].replace(",", "")] % 2 == 0:
                pos += jump(instruction.split(" ")[2])
            else:
                pos += 1
        elif i == "jio":
            if register[instruction.split(" ")[1].replace(",", "")] == 1:
                pos += jump(instruction.split(" ")[2])
            else:
                pos += 1
    return register


with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]
    print("Answer 1: " + str(runProcess({'a': 0, 'b': 0})['b']))
    print("Answer 2: " + str(runProcess({'a': 1, 'b': 0})['b']))
