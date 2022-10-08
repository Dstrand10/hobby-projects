import numpy as np


class Cube:

    def __init__(self, x_range, y_range, z_range):
        self.x_min = x_range[0]
        self.x_max = x_range[1]
        self.y_min = y_range[0]
        self.y_max = y_range[1]
        self.z_min = z_range[0]
        self.z_max = z_range[1]


def func1(data):
    G = np.zeros((101, 101, 101))
    for row in data:
        row = row.split(",")
        on = row[0].split(" ")[0] == "on"
        x_range = list(map(int, row[0].split("=")[1].split("..")))
        y_range = list(map(int, row[1].split("=")[1].split("..")))
        z_range = list(map(int, row[2].split("=")[1].split("..")))
        if x_range[0] > 50 or x_range[0] < -50:
            continue
        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                for z in range(z_range[0], z_range[1] + 1):
                    if on:
                        G[x][y][z] = 1
                    elif not on:
                        G[x][y][z] = 0
    return G.sum()


def getSubranges(control_range, low, high):
    if control_range[-1] < low or control_range[0] > high:
        return None
    return range(max(control_range[0], low), min(control_range[-1], high) + 1)


def calculateLitCubes(volumeCube, volumeCubes):
    on, x_range, y_range, z_range = volumeCube

    total = len(x_range) * len(y_range) * len(z_range)

    conflicts = []
    for vc_rest in volumeCubes:
        on, cx, cy, cz = vc_rest
        cx_range = getSubranges(cx, x_range[0], x_range[-1])
        cy_range = getSubranges(cy, y_range[0], y_range[-1])
        cz_range = getSubranges(cz, z_range[0], z_range[-1])
        if cx_range is None or cy_range is None or cz_range is None:
            continue
        conflicts.append((on, cx_range, cy_range, cz_range))

    for id, conflict in enumerate(conflicts):
        total -= calculateLitCubes(conflict, conflicts[id+1:])

    return total



def func2(data):

    volumeCubes = []
    for row in data:
        row = row.split(",")
        on = row[0].split(" ")[0] == "on"
        x_range = range(int(row[0].split("=")[1].split("..")[0]), int(row[0].split("=")[1].split("..")[1]) + 1)
        y_range = range(int(row[1].split("=")[1].split("..")[0]), int(row[1].split("=")[1].split("..")[1]) + 1)
        z_range = range(int(row[2].split("=")[1].split("..")[0]), int(row[2].split("=")[1].split("..")[1]) + 1)
        volumeCubes.append((on, x_range, y_range, z_range))

    ans = 0
    for idx, volumeCube in enumerate(volumeCubes):
        on, x_range, y_range, z_range = volumeCube
        if not on:
            continue #Not turning on off-cubes
        ans += calculateLitCubes(volumeCube, volumeCubes[idx + 1:])
    return ans



def main():
    data = open("input.txt").read().split("\n")

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
