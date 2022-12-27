def func1(data):
    cnt = 0
    DIR = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for coord in data:
        for i in range(6):
            x = coord[0] + DIR[i][0]
            y = coord[1] + DIR[i][1]
            z = coord[2] + DIR[i][2]
            if not (x, y, z) in data:
                cnt += 1
    return cnt


def bfs_node_within(coord, data, maxCoords):
    visited = [coord]
    queue = [coord]
    is_drops = True
    DIR = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while queue:  # Creating loop to visit each node
        for i in range(6):
            x = queue[0][0] + DIR[i][0]
            y = queue[0][1] + DIR[i][1]
            z = queue[0][2] + DIR[i][2]
            if maxCoords[0] <= x <= maxCoords[1] and maxCoords[2] <= y <= maxCoords[3] and maxCoords[4] <= z <= \
                    maxCoords[5]:
                if (x, y, z) not in visited and (x, y, z) not in data:
                    visited.append((x, y, z))
                    queue.append((x, y, z))
            else:
                is_drops = False
        queue.pop(0)
    return is_drops, visited


def checkIfCoordInList(coord, listoflistofcoords):
    for listofcoords in listoflistofcoords:
        if coord in listofcoords:
            return True
    return False


def calculateSharedSidesLavaDrops(alreadyFoundDrops, data):
    cnt = 0
    for drops in alreadyFoundDrops:
        DIR = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        for coord in drops:
            for i in range(6):
                x = coord[0] + DIR[i][0]
                y = coord[1] + DIR[i][1]
                z = coord[2] + DIR[i][2]
                if (x, y, z) in data:
                    cnt += 1
    return cnt


def func2(data):
    min_x = min([coord[0] for coord in data])
    max_x = max([coord[0] for coord in data])
    min_y = min([coord[1] for coord in data])
    max_y = max([coord[1] for coord in data])
    min_z = min([coord[2] for coord in data])
    max_z = max([coord[2] for coord in data])
    maxCoords = (min_x, max_x, min_y, max_y, min_z, max_z)
    not_drop_coords = []
    alreadyFoundDrops = []
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            for k in range(min_z, max_z):
                if (i, j, k) not in data and not checkIfCoordInList((i, j, k),
                                                                    alreadyFoundDrops) and not checkIfCoordInList(
                        (i, j, k), not_drop_coords):
                    are_drops, coords = bfs_node_within((i, j, k), data, maxCoords)
                    if are_drops:
                        alreadyFoundDrops.append(coords.copy())
                    else:
                        not_drop_coords.append(coords.copy())
    return calculateSharedSidesLavaDrops(alreadyFoundDrops, data)



def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]
    tmp_data = []
    for row in data:
        tmp_data.append((int(row.split(",")[0]), int(row.split(",")[1]), int(row.split(",")[2])))
    data = tmp_data
    print(data)
    sol1 = func1(data)
    print(f"Solution 1: {sol1}")


    sides_inside_lava_ball = func2(data)
    sol2 = sol1 - sides_inside_lava_ball
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
