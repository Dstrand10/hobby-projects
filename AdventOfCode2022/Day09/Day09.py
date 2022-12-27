def updateTail(H, T):
    DR = H[0] - T[0]
    DC = H[1] - T[1]
    if abs(DR) <= 1 and abs(DC) <= 1:
        pass
    elif abs(DR) >= 2 and abs(DC) >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1] - 1 if T[1] < H[1] else H[1] + 1)
    elif abs(DR) >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])
    elif abs(DC) >= 2:
        T = (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)
    return T


def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").readlines()
    # data = [row.split() for row in data]

    HT = [(0, 0) for _ in range(10)]
    dr = {"R": 0, "D": 1, "L": 0, "U": -1}
    dc = {"R": 1, "D": 0, "L": -1, "U": 0}
    sol1 = set()
    sol2 = set()
    for row in data:
        dir, nbr = row.strip().split()
        nbr = int(nbr)
        for _ in range(nbr):
            HT[0] = (HT[0][0] + dr[dir], HT[0][1] + dc[dir])
            for i in range(1, 10):
                HT[i] = updateTail(HT[i - 1], HT[i])
            sol1.add(HT[1])
            sol2.add(HT[-1])

    print(f"Solution 1: {len(sol1)}")
    print(f"Solution 2: {len(sol2)}")


if __name__ == "__main__":
    main()
