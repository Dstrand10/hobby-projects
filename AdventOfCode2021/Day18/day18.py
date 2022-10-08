import itertools
import math
from functools import reduce


def calcMagnitude(x):
    if isinstance(x, int):
        return x
    return 3 * calcMagnitude(x[0]) + 2 * calcMagnitude(x[1])


def add_left(x, right_nbr):
    if right_nbr is None:
        return x
    if isinstance(x, int):
        return x + right_nbr
    return [add_left(x[0], right_nbr), x[1]]


def add_right(x, left_nbr):
    if left_nbr is None:
        return x
    if isinstance(x, int):
        return x + left_nbr
    return [x[0], add_right(x[1], left_nbr)]


def explode(x, n=4):
    if isinstance(x, int):
        return False, x, None, None
    if n == 0:
        return True, 0, x[0], x[1]
    x1, x2 = x
    change, x1, left, right = explode(x1, n - 1)
    if change:
        returnList = [x1, add_left(x2, right)]
        return True, returnList, left, None
    change, x2, left, right = explode(x2, n - 1)
    if change:
        returnList = [add_right(x1, left), x2]
        return True, returnList, None, right
    return False, x, None, None



def trySplit(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [math.floor(x/2), math.ceil(x/2)]
        return False, x
    change, x[0] = trySplit(x[0])
    if change:
        return True, x
    change, x[1] = trySplit(x[1])
    return change, x


def add(x, y):
    l = [x, y]
    while True:
        change, l, _, _ = explode(l)
        if change:
            continue
        change, l = trySplit(l)
        if change:
            continue
        else:
            break
    return l



def main():
    lines = list(map(eval, open("input.txt").read().split("\n")))
    sol1 = calcMagnitude(reduce(add, lines))
    print("Solution 1:" + str(sol1))
    sol2 = max(calcMagnitude(add(a, b)) for a, b in itertools.permutations(lines, 2))
    print("Solution 2:" + str(sol2))


if __name__ == "__main__":
    main()
