def transformCodeToString(line):
    line = line[1:-1]
    transformedLine = ""
    while len(line) > 0:
        char = line[0]
        if char == "\\":
            if line[1] == "\\":
                transformedLine += "\\"
                line = line[2:]
            elif line[1] == "\"":
                transformedLine += "\""
                line = line[2:]
            elif line[1] == "x":
                transformedLine += chr(int(line[2:4], 16))  # calculate ascii letter
                line = line[4:]
            else:
                EOFError
        else:
            transformedLine += char
            line = line[1:]
    return transformedLine


def transformStringToCode(line):
    transformedLine = ""
    while len(line) > 0:
        char = line[0]
        if char == "\"":
            transformedLine += "\\\""
            line = line[1:]
        elif char == "\\":
            transformedLine += "\\\\"
            line = line[1:]
        else:
            transformedLine += char
            line = line[1:]
    return "\"" + transformedLine + "\""


with open("input.txt") as f:
    totCharsCode = 0
    totCharsString = 0
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        transformedCodeToString = transformCodeToString(line)
        codeLength = len(line)
        stringLength = len(transformedCodeToString)
        totCharsCode += codeLength
        totCharsString += stringLength
    print("Answer 1: " + str(totCharsCode-totCharsString))

    totCharsCode = 0
    totCharsString = 0
    for line in lines:
        line = line.replace("\n", "")
        transformedStringToCode = transformStringToCode(line)
        stringLength = len(line)
        codeLength = len(transformedStringToCode)
        totCharsString += stringLength
        totCharsCode += codeLength
    print("Answer 2: " + str(totCharsCode - totCharsString))