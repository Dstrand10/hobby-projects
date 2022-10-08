from collections import deque
import numpy as np


class MyClass:

    def __init__(self):
        pass


def func1(in_data):
    R = len(in_data)
    C = len(in_data[0])

    start = [((0, 0), 0)]
    Q = deque(start)
    DR = [1, 0, -1, 0]
    UC = [0, 1, 0, -1]

    ans = 100000000
    while Q:
        pos, val = Q.popleft()
        if pos == (R - 1, C - 1):
            if val < ans:
                ans = val
            continue

        for d in range(4):
            if 0 <= pos[0] + DR[d] < R and 0 <= pos[1] + UC[d] < C and in_data[pos[0] + DR[d]][pos[1] + UC[d]] > 0:
                new_pos = (pos[0] + DR[d], pos[1] + UC[d])
                new_val = val + in_data[new_pos[0]][new_pos[1]]
                in_data[new_pos[0]][new_pos[1]] = -1
                Q.append((new_pos, new_val))



    return ans


def func2(in_data):
    pass


def buildIndata2(in_data):
    R = len(in_data)
    C = len(in_data[0])
    large_tile = np.zeros((5 * R, 5 * C))
    orig_tile = np.zeros((len(in_data), len(in_data[0])))

    for rowid, row in enumerate(in_data):
        for colid, nbr in enumerate(row):
            orig_tile[rowid][colid] = nbr
            large_tile[rowid][colid] = nbr

    new_tile = orig_tile.copy()

    for i in range(1, 5):
        for rowid, row in enumerate(new_tile):
            for colid, nbr in enumerate(row):
                new_tile[rowid][colid] = (nbr + 1) if (nbr + 1) < 10 else 1
        for rowid, row in enumerate(new_tile):
            for colid, nbr in enumerate(row):
                large_tile[rowid][colid + i * C] = nbr
    new_tile_row = large_tile[:R, :].copy()

    for i in range(1, 5):
        for rowid, row in enumerate(new_tile_row):
            for colid, nbr in enumerate(row):
                new_tile_row[rowid][colid] = (nbr + 1) if (nbr + 1) < 10 else 1
        for rowid, row in enumerate(new_tile_row):
            for colid, nbr in enumerate(row):
                large_tile[rowid + i * R][colid] = nbr
    return large_tile

def main():
    in_data = open("input.txt").read().split("\n")
    in_data = [list(map(int, x)) for x in in_data]

    # sol1 = func1(in_data)
    # print(f"Solution 1: {sol1}")

    in_data_2 = buildIndata2(in_data)

    sol2 = func1(in_data_2)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
