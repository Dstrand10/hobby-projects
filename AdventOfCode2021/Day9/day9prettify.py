from collections import deque


def main():
    with open("input.txt") as f:
        tot = 0
        G = [list(map(int, x)) for x in f.read().split("\n")]
        R = len(G)
        C = len(G[0])
        LR = [-1, 0, 1, 0]
        UD = [0, 1, 0, -1]
        for y in range(R):
            for x in range(C):
                is_ok = True
                for d in range(4):
                    y_test = y + UD[d]
                    x_test = x + LR[d]
                    if 0 <= y_test < R and 0 <= x_test < C and G[y_test][x_test] <= G[y][x]:
                        is_ok = False
                        break
                if is_ok:
                    tot += 1 + G[y][x]
        print("Solution 1: " + str(tot))


        seen = set()
        S = []

        for y in range(R):
            for x in range(C):
                if (y, x) not in seen and G[y][x] != 9:
                    size = 0
                    Q = deque()
                    Q.append((y, x))
                    while Q:
                        (y, x) = Q.popleft()
                        if (y, x) in seen:
                            continue
                        seen.add((y, x))
                        size += 1
                        for d in range(4):
                            y_test = y + UD[d]
                            x_test = x + LR[d]
                            if 0 <= y_test < R and 0 <= x_test < C and G[y_test][x_test] != 9:
                                Q.append((y_test, x_test))
                    S.append(size)
        S.sort()
        print(S[-1] * S[-2] * S[-3])






if __name__ == "__main__":
    main()
