file = open("Day2Input1", "r")

if file.mode == "r":
    content = file.read()
    intCode = list(map(int, content.split(",")))


def addFunction(list, row):
    secondOnRow = list[4 * row + 1]
    thirdOnRow = list[4 * row + 2]
    fourthOnRow = list[4 * row + 3]
    list[fourthOnRow] = list[secondOnRow] + list[thirdOnRow]
    return list


def multiplyFunction(list, row):
    secondOnRow = list[4 * row + 1]
    thirdOnRow = list[4 * row + 2]
    fourthOnRow = list[4 * row + 3]
    list[fourthOnRow] = list[secondOnRow] + list[thirdOnRow]
    list[fourthOnRow] = list[secondOnRow] * list[thirdOnRow]
    return list


def readIntCode(list):
    row = 0
    while True:
        first = 4 * row
        if list[first] == 1:
            list = addFunction(list, row)
            row += 1
        elif list[first] == 2:
            list = multiplyFunction(list, row)
            row += 1
        elif list[first] == 99:
            return list
        else:
            print("Error, this should not happen if the intCode is right")


list = [1, 0, 0, 0, 99]
print(readIntCode(list))
list = [2, 3, 0, 3, 99]
print(readIntCode(list))
list = [2, 4, 4, 5, 99, 0]
print(readIntCode(list))
list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
print(readIntCode(list))
print(readIntCode(intCode))

# Part 2

for i in range(1, 100):
    for j in range(1, 100):
        list = [1, i, j, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 9, 19, 1, 19, 5, 23, 2, 6, 23, 27, 1, 6, 27, 31,
                2, 31, 9, 35, 1, 35, 6, 39, 1, 10, 39, 43, 2, 9, 43, 47, 1, 5, 47, 51, 2, 51, 6, 55, 1, 5, 55, 59, 2,
                13, 59, 63, 1, 63, 5, 67, 2, 67, 13, 71, 1, 71, 9, 75, 1, 75, 6, 79, 2, 79, 6, 83, 1, 83, 5, 87, 2, 87,
                9, 91, 2, 9, 91, 95, 1, 5, 95, 99, 2, 99, 13, 103, 1, 103, 5, 107, 1, 2, 107, 111, 1, 111, 5, 0, 99, 2,
                14, 0, 0]
        if readIntCode(list)[0] == 19690720:
            print(list)
            print(i)
            print(j)
            print(i*100 + j)