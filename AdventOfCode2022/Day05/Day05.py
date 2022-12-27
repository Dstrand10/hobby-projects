from collections import defaultdict


def func1(moves, crates):
    for move in moves.split("\n"):
        moveSplit = move.split(" ")
        moveNumber = int(moveSplit[1])
        moveFrom = int(moveSplit[3])
        moveTo = int(moveSplit[-1])

        movingCrates = crates[moveFrom]
        tmp_list = movingCrates[:moveNumber]
        tmp_list.reverse()
        crates[moveTo] = tmp_list + crates[moveTo]
        crates[moveFrom] = movingCrates[moveNumber:]
    return crates[1][0] + crates[2][0] + crates[3][0] + crates[4][0] + crates[5][0] + crates[6][0] + crates[7][0] + \
           crates[8][0] + crates[9][0]


def func2(moves, crates):
    for move in moves.split("\n"):
        moveSplit = move.split(" ")
        moveNumber = int(moveSplit[1])
        moveFrom = int(moveSplit[3])
        moveTo = int(moveSplit[-1])

        movingCrates = crates[moveFrom]
        tmp_list = movingCrates[:moveNumber]
        crates[moveTo] = tmp_list + crates[moveTo]
        crates[moveFrom] = movingCrates[moveNumber:]
    return crates[1][0] + crates[2][0] + crates[3][0] + crates[4][0] + crates[5][0] + crates[6][0] + crates[7][0] + \
           crates[8][0] + crates[9][0]


def getCrates(data):
    one = (1, data[-1].index('1'))
    two = (2, data[-1].index('2'))
    three = (3, data[-1].index('3'))
    four = (4, data[-1].index('4'))
    five = (5, data[-1].index('5'))
    six = (6, data[-1].index('6'))
    seven = (7, data[-1].index('7'))
    eight = (8, data[-1].index('8'))
    nine = (9, data[-1].index('9'))
    positions = [one, two, three, four, five, six, seven, eight, nine]
    crates = defaultdict(list)

    for row in data[:-1]:
        for name, pos in positions:
            if pos < len(row) and row[pos] != ' ':
                tmp_list = crates.get(name, list())
                tmp_list.append(row[pos])
                crates[name] = tmp_list
    return crates


def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n\n")
    # data = [row.split() for row in data]

    crates = getCrates(data[0].split("\n"))

    sol1 = func1(data[1], crates.copy())
    print(f"Solution 1: {sol1}")

    sol2 = func2(data[1], crates.copy())
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
