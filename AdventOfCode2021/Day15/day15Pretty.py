#--- Runtime 5 min ---

import numpy as np

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


def findNextNode(visitedNodes):
    for i in range(len(visitedNodes)):
        for j in range(len(visitedNodes[0])):
            if visitedNodes[i][j] == 0:
                return i, j
    return None, None


def findSmallestUnvisitedNode(s_next_to_visit, travelCost):
    node_ret = None
    max_val = np.amax(travelCost)
    for node in s_next_to_visit:
        if travelCost[node[0]][node[1]] <= max_val:
            max_val = travelCost[node[0]][node[1]]
            node_ret = node
    s_next_to_visit.remove(node_ret)
    return node_ret


def shortestPath(in_data):
    data = np.array(in_data)
    R = len(data)
    C = len(data[0])

    visitedNodes = np.zeros(data.shape)
    visitedNodes[0][0] = 1
    travelCost = np.ones(data.shape) * data.sum()
    travelCost[0][0] = 0

    DR = [0, -1, 0, 1]
    DC = [1, 0, -1, 0]
    s_next_to_visit = set()
    current_node = (0, 0)
    while visitedNodes.sum() < R * C:
        i = current_node[0]
        j = current_node[1]
        if i == R - 1 and j == C - 1:
            return travelCost[-1][-1]
        for d in range(4):
            adj_rowid = i + DR[d]
            adj_colid = j + DC[d]
            if 0 <= adj_rowid < R and 0 <= adj_colid < C and visitedNodes[adj_rowid][adj_colid] == 0 and \
                    travelCost[adj_rowid][adj_colid] > travelCost[i][j] + data[adj_rowid][adj_colid]:
                travelCost[adj_rowid][adj_colid] = travelCost[i][j] + data[adj_rowid][adj_colid]
            if 0 <= adj_rowid < R and 0 <= adj_colid < C and visitedNodes[adj_rowid][adj_colid] != 1:
                s_next_to_visit.add((adj_rowid, adj_colid))
        visitedNodes[i][j] = 1
        if visitedNodes[-1][-1] == 1:
            return travelCost[-1][-1]
        else:
            current_node = findSmallestUnvisitedNode(s_next_to_visit, travelCost)


data = [list(map(int, line.strip())) for line in open("input.txt").readlines()]

print(f"Solution 1: {shortestPath(data)}")

in_data_2 = buildIndata2(data)

print(f"Solution 2: {shortestPath(in_data_2)}")
