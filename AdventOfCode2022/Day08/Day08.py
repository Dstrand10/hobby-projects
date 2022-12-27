import numpy as np


def getVisibleAndScenicScore(height, dataList):
    lowerTreeLogical = [i < height for i in dataList]
    visible = False
    if all(i for i in lowerTreeLogical):
        visible = True
    if False in lowerTreeLogical:
        multScenicScore = lowerTreeLogical.index(False) + 1
    else:
        multScenicScore = len(lowerTreeLogical)
    return visible, multScenicScore


def solve(data):
    visible = dict()
    for idx, rr in enumerate(data):
        for idy, cc in enumerate(rr):
            if idx == 0 or idx == len(data) - 1:
                visible[idx, idy] = 0
                continue
            elif idy == 0 or idy == len(rr) - 1:
                visible[(idx, idy)] = 0
                continue
            scenicScore = 1
            visibleBoolean = False
            for i in range(4):
                if i == 0:
                    visibleGotten, multScenicScore = getVisibleAndScenicScore(int(cc), data[idx, idy + 1:])
                    if visibleGotten:
                        visibleBoolean = visibleGotten
                    scenicScore *= multScenicScore
                elif i == 1:
                    visibleGotten, multScenicScore = getVisibleAndScenicScore(int(cc), data[idx + 1:, idy])
                    if visibleGotten:
                        visibleBoolean = visibleGotten
                    scenicScore *= multScenicScore
                elif i == 2:
                    reversed_data = list(data[idx, :idy])
                    reversed_data.reverse()
                    visibleGotten, multScenicScore = getVisibleAndScenicScore(int(cc), reversed_data)
                    if visibleGotten:
                        visibleBoolean = visibleGotten
                    scenicScore *= multScenicScore
                else:
                    reversed_data = list(data[:idx, idy])
                    reversed_data.reverse()
                    visibleGotten, multScenicScore = getVisibleAndScenicScore(int(cc), reversed_data)
                    if visibleGotten:
                        visibleBoolean = visibleGotten
                    scenicScore *= multScenicScore
            if visibleBoolean:
                visible[(idx, idy)] = scenicScore

    return visible


def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data_raw = open("input.txt").read().split("\n")
    data = np.zeros((len(data_raw), len(data_raw[0])))
    for idx, row in enumerate(data_raw):
        for idy, col in enumerate(row):
            data[idx, idy] = int(col)
    # data = [row.split() for row in data]

    solution = solve(data)
    print(f"Solution 1: {len(solution)}")
    print(f"Solution 2: {max([val for _, val in solution.items()])}")


if __name__ == "__main__":
    main()
