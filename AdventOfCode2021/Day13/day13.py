import numpy as np

def func2(coords):
    x_min = min([coord[0] for coord in coords])
    y_min = min([coord[1] for coord in coords])
    x_max = max([coord[0] for coord in coords])
    y_max = max([coord[1] for coord in coords])

    matrix = np.zeros((y_max + 1 - y_min, x_max + 1 - x_min))
    for coord in coords:
        matrix[coord[1]][coord[0]] = 1
    for row in matrix:
        row_string = ''
        for nbr in row:
            if nbr == 0:
                row_string = row_string + " "
            else:
                row_string = row_string + "#"
        print(row_string)


def foldXat(coords, nbr):
    copy_set = coords.copy()
    for coord in copy_set:
        x = coord[0]
        y = coord[1]
        if x > nbr:
            new_x = nbr - (x - nbr)
            coords.remove(coord)
            coords.add((new_x, y))


def foldYat(coords, nbr):
    copy_set = coords.copy()
    for coord in copy_set:
        x = coord[0]
        y = coord[1]
        if y > nbr:
            new_y = nbr - (y - nbr)
            coords.remove(coord)
            coords.add((x, new_y))


def main():
    in_data = open("inputHarder.txt").read().split("\n\n")
    #in_data = open("input.txt").read().split("\n\n")

    coords = set()
    for line in in_data[0].split("\n"):
        a, b = line.split(",")
        coords.add((int(a), int(b)))

    first_fold = True
    for row in in_data[1].split("\n"):
        exec, nbr = row.split("=")
        if "x" in exec:
            foldXat(coords, int(nbr))
        elif "y" in exec:
            foldYat(coords, int(nbr))
        if first_fold:
            sol1 = len(coords)
            first_fold = False

    print(f"Solution 1: {sol1}")

    print(f"Solution 2: ")
    func2(coords)


if __name__ == "__main__":
    main()
