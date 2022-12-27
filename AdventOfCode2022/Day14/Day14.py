from collections import defaultdict


def solve(rock_coords):
    deepest_rock = max([k[1] for k, v in rock_coords.items()]) + 2
    sand_coords = defaultdict(int)
    new_sand = True
    part1 = None
    while True:
        if new_sand:
            sand_coord = (500, 0)
            new_sand = False
        # Get part 1 when
        if part1 is None and sand_coord[1] == deepest_rock - 2:
            part1 = len(sand_coords)

        if sand_coord[1] == deepest_rock:
            sand_coords[sand_coord[0], sand_coord[1] - 1] = 1
            new_sand = True
        elif (sand_coord[0], sand_coord[1] + 1) not in rock_coords.keys() and (
        sand_coord[0], sand_coord[1] + 1) not in sand_coords.keys():
            sand_coord = (sand_coord[0], sand_coord[1] + 1)
        elif (sand_coord[0] - 1, sand_coord[1] + 1) not in rock_coords.keys() and (
        sand_coord[0] - 1, sand_coord[1] + 1) not in sand_coords.keys():
            sand_coord = (sand_coord[0] - 1, sand_coord[1] + 1)
        elif (sand_coord[0] + 1, sand_coord[1] + 1) not in rock_coords.keys() and (
        sand_coord[0] + 1, sand_coord[1] + 1) not in sand_coords.keys():
            sand_coord = (sand_coord[0] + 1, sand_coord[1] + 1)
        else:
            sand_coords[sand_coord] = 1
            new_sand = True
        if sand_coord == (500, 0):
            break
    return part1, len(sand_coords)


def getRockCords(data):
    rock_coords = defaultdict(int)
    for row in data:
        row_split = row.split(" -> ")
        for i in range(len(row_split) - 1):
            coord1 = list(map(int, row_split[i].split(",")))
            coord2 = list(map(int, row_split[i+1].split(",")))
            if coord1[0] - coord2[0] != 0:
                for j in range(min(coord1[0],coord2[0]), max(coord1[0], coord2[0]) + 1):
                    rock_coords[(j, coord1[1])] = 1
            elif coord1[1] - coord2[1] != 0:
                for j in range(min(coord1[1],coord2[1]), max(coord1[1], coord2[1]) + 1):
                    rock_coords[(coord1[0], j)] = 1
    return rock_coords


def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    rock_coords = getRockCords(data)
    sol1, sol2 = solve(rock_coords)
    print(f"Solution 1: {sol1}")
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
