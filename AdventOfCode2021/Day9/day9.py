class Basin:

    def __init__(self, in_data):
        self.bottom_grid = [list(map(int, row)) for row in in_data]
        self.smallestPoints = self.LocateSmallestPoints()
        self.basins = self.findBasins()


    def LocateSmallestPoints(self):
        smallest_points = []
        for idy, row in enumerate(self.bottom_grid):
            for idx, pos in enumerate(row):
                pos = int(pos)
                if idy == 0 and idx == 0:
                    if int(pos) < int(row[idx + 1]) and int(pos) < int(self.bottom_grid[idy + 1][idx]):
                        smallest_points.append((idy, idx))
                elif idy == 0 and idx == len(row) - 1:
                    if int(pos) < int(row[idx - 1]) and int(pos) < int(self.bottom_grid[idy + 1][idx]):
                        smallest_points.append((idy, idx))
                elif idy == 0:
                    if pos < int(row[idx - 1]) and pos < int(self.bottom_grid[idy + 1][idx]) and pos < int(row[idx + 1]):
                        smallest_points.append((idy, idx))
                elif idy == len(self.bottom_grid) - 1 and idx == 0:
                    if pos < int(row[idx + 1]) and pos < int(self.bottom_grid[idy - 1][idx]):
                        smallest_points.append((idy, idx))
                elif idy == len(self.bottom_grid) - 1 and idx == len(row) - 1:
                    if pos < int(row[idx - 1]) and pos < int(self.bottom_grid[idy - 1][idx]):
                        smallest_points.append((idy, idx))
                elif idy == len(self.bottom_grid) - 1:
                    if pos < int(row[idx - 1]) and pos < int(self.bottom_grid[idy - 1][idx]) and pos < int(row[idx + 1]):
                        smallest_points.append((idy, idx))
                elif idx == 0:
                    if pos < int(self.bottom_grid[idy - 1][idx]) and pos < int(row[idx + 1]) and pos < int(
                            self.bottom_grid[idy + 1][idx]):
                        smallest_points.append((idy, idx))
                elif idx == len(row) - 1:
                    if pos < int(self.bottom_grid[idy - 1][idx]) and pos < int(row[idx - 1]) and pos < int(
                            self.bottom_grid[idy + 1][idx]):
                        smallest_points.append((idy, idx))
                else:
                    if pos < int(self.bottom_grid[idy - 1][idx]) and pos < int(self.bottom_grid[idy + 1][idx]) and pos < int(
                            row[idx - 1]) and pos < int(row[idx + 1]):
                        smallest_points.append((idy, idx))
        return smallest_points

    def findBasins(self):
        basins = []
        for id, smallpoint in enumerate(self.smallestPoints):
            tmp_basin = []
            tmp_basin.append(smallpoint)

            while True:
                nbrsAppended = 0
                nextPoints = self.findNextPoints(tmp_basin)
                for nextPoint in nextPoints:
                    if nextPoint not in tmp_basin:
                        tmp_basin.append(nextPoint)
                        nbrsAppended = +1
                if nbrsAppended == 0:
                    break
            basins.append(tmp_basin)
        return basins

    def findNextPoints(self, points):
        nextPoints = []

        for point in points:
            pointsToCheck = [(point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0] + 1, point[1]), (point[0], point[1] - 1)]
            for pointToCheck in pointsToCheck:
                if int(pointToCheck[0]) < 0 or int(pointToCheck[0]) > len(self.bottom_grid) - 1 or int(pointToCheck[1]) < 0 or int(pointToCheck[1]) > len(self.bottom_grid[0]) - 1:
                    continue
                nextPointHeigh = self.bottom_grid[pointToCheck[0]][pointToCheck[1]]
                pointHeight = self.bottom_grid[point[0]][point[1]]

                if nextPointHeigh == 9:
                    continue
                if nextPointHeigh > pointHeight:
                    nextPoints.append(pointToCheck)
        return nextPoints

    def calculate3LargestBasins(self):
        basinSize = []
        for basin in self.basins:
            basinSize.append(len(basin))
        return sorted(basinSize)[len(basinSize) - 1] * sorted(basinSize)[len(basinSize) - 2] * sorted(basinSize)[len(basinSize) - 3]



def func1(in_data):
    total = 0
    for idy, row in enumerate(in_data):
        for idx, pos in enumerate(row):
            pos = int(pos)
            if idy == 0 and idx == 0:
                if int(pos) < int(row[idx + 1]) and int(pos) < int(in_data[idy + 1][idx]):
                    total += int(pos) + 1
            elif idy == 0 and idx == len(row) - 1:
                if int(pos) < int(row[idx - 1]) and int(pos) < int(in_data[idy + 1][idx]):
                    total += int(pos) + 1
            elif idy == 0:
                if pos < int(row[idx - 1]) and pos < int(in_data[idy + 1][idx]) and pos < int(row[idx + 1]):
                    total += pos + 1
            elif idy == len(in_data) - 1 and idx == 0:
                if pos < int(row[idx + 1]) and pos < int(in_data[idy - 1][idx]):
                    total += pos + 1
            elif idy == len(in_data) - 1 and idx == len(row) - 1:
                if pos < int(row[idx - 1]) and pos < int(in_data[idy - 1][idx]):
                    total += pos + 1
            elif idy == len(in_data) - 1:
                if pos < int(row[idx - 1]) and pos < int(in_data[idy - 1][idx]) and pos < int(row[idx + 1]):
                    total += pos + 1
            elif idx == 0:
                if pos < int(in_data[idy - 1][idx]) and pos < int(row[idx + 1]) and pos < int(in_data[idy + 1][idx]):
                    total += pos + 1
            elif idx == len(row) - 1:
                if pos < int(in_data[idy - 1][idx]) and pos < int(row[idx - 1]) and pos < int(in_data[idy + 1][idx]):
                    total += pos + 1
            else:
                if pos < int(in_data[idy - 1][idx]) and pos < int(in_data[idy + 1][idx]) and pos < int(row[idx - 1]) and pos < int(row[idx + 1]) :
                    total += pos + 1
    return total

def func2(in_data):
    basin = Basin(in_data)
    return basin.calculate3LargestBasins()

def main():
    with open('input.txt') as f:
        in_data = f.read().split("\n")

        sol1 = func1(in_data)
        print(f"Solution 1: {sol1}")

        sol2 = func2(in_data)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
