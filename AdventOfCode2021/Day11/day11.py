import numpy as np

class FlashGrid:

    def __init__(self, grid):
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        self.flashed = np.zeros((self.R, self.C))
        self.DR = [-1, -1, 0, 1, 1, 1, 0, -1]
        self.DC = [0, -1, -1, -1, 0, 1, 1, 1]
        self.total_flashes = 0
        self.all_flashed = False

    def iterate(self):
        for idy in range(self.R):
            for idx in range(self.C):
                if self.flashed[idy][idx] == 0:
                    self.grid[idy][idx] += 1
                if self.grid[idy][idx] > 9:
                    self.total_flashes += 1
                    self.grid[idy][idx] = 0
                    self.flashed[idy][idx] = 1
                    self.flashAdjacent((idy, idx))
        self.all_flashed = self.allFlashed()
        self.flashed = np.zeros((self.R, self.C))

    def flashAdjacent(self, point):
        for d in range(8):
            adj_r = point[0] + self.DR[d]
            adj_c = point[1] + self.DC[d]
            if 0 <= adj_r < self.R and 0 <= adj_c < self.C and self.flashed[adj_r][adj_c] == 0:
                self.grid[adj_r][adj_c] += 1
                if self.grid[adj_r][adj_c] > 9:
                    self.total_flashes += 1
                    self.grid[adj_r][adj_c] = 0
                    self.flashed[adj_r][adj_c] = 1
                    self.flashAdjacent((adj_r, adj_c))

    def allFlashed(self):
        for r in self.flashed:
            for c in r:
                if c == 0:
                    return False
        return True


def func2(in_data):
    R = len(in_data)
    C = len(in_data[0])
    G = np.zeros((R, C))
    for idy in range(R):
        for idx in range(C):
            G[idy][idx] = int(in_data[idy][idx])

    fg = FlashGrid(G)
    all_flashed = False
    i = 0
    while not all_flashed:
        i += 1
        fg.iterate()
        all_flashed = fg.all_flashed

    return i


def func1(in_data):
    R = len(in_data)
    C = len(in_data[0])
    G = np.zeros((R, C))
    for idy in range(R):
        for idx in range(C):
            G[idy][idx] = int(in_data[idy][idx])

    fg = FlashGrid(G)
    for i in range(100):
        fg.iterate()

    return fg.total_flashes








def main():
    in_data = open("input.txt").read().split("\n")
    print([list(map(int, x)) for x in in_data])

    sol1 = func1(in_data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(in_data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
