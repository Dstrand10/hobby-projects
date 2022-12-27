import math
from collections import defaultdict
from heapq import heappop, heappush


def func1(data, S):
    R = len(data)
    C = len(data[0])

    Q = [(0, S[0], S[1])]
    travelCost = defaultdict(int)
    travelCost[S] = 0

    DIR = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while Q:
        dist, rowid, colid = heappop(Q)
        if data[rowid][colid] == "E":
            return dist

        if 0 > rowid or rowid >= R or 0 > colid or colid >= C:
            continue

        for d in range(4):
            rr = rowid + DIR[d][0]
            cc = colid + DIR[d][1]
            if 0 > rr or rr >= R or 0 > cc or cc >= C:
                continue
            currentElev = ord("a") if data[rowid][colid] == "S" else ord(data[rowid][colid])
            nextElev = ord("z") if data[rr][cc] == "E" else ord(data[rr][cc])
            if 0 <= rr < R and 0 <= cc < C and travelCost.get((rr, cc),
                                                              math.inf) > dist + 1 and nextElev - currentElev <= 1:
                travelCost[(rr, cc)] = dist + 1
                heappush(Q, (dist + 1, rr, cc))


def func2(data):
    pos_trails = list()
    for rowid, row in enumerate(data):
        for colid, col in enumerate(row):
            if col == "a":
                shortest_path = func1(data, (rowid, colid))
                if shortest_path is not None:
                    pos_trails.append(shortest_path)
    return min(pos_trails)



def bfs(data, node):  # function for BFS
    visited = [node]
    queue = [node]
    cnt = 0

    DIR = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while queue:  # Creating loop to visit each node
        if data[node[0]][node[1]] == "E":
            return cnt
        cnt += 1

        for i in range(4):
            DR = node[0] + DIR[i][0]
            DC = node[1] + DIR[i][1]
            if 0 <= DR < len(data) and 0 <= DC <= len(data[0]):
                if (DR, DC) not in visited and ord("z") if data[DR][DC] == "E" else ord(data[DR][DC]) - ord("a") if data[node[0]][node[1]] == "S" else ord(data[node[0]][node[1]]):
                    visited.append((DR, DC))
                    queue.append((DR, DC))


def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    S = None
    for rowid, row in enumerate(data):
        if "S" in row:
            S = (rowid, row.index("S"))

    sol1 = func1(data, S)
    print(f"Solution 1: {sol1}")

    sol1 = bfs(data, S)
    print(f"Solution 1 (bfs): {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
