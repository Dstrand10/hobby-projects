import math

file = open("Day3Input1", "r")

if file.mode == "r":
    content = file.read()
    rows = content.splitlines()
    line1 = rows[0].split(",")
    line2 = rows[1].split(",")
    print(line1)
    print(line2)


def calculateLineCoordinates(line):
    currentX = 0
    currentY = 0
    allLineCordinates = [(currentX, currentY)]
    for instruction in line:
        direction = instruction[0]
        distance = int(instruction[1:]) + 1
        if direction == 'R':
            for count in range(1, distance):
                currentX += 1
                allLineCordinates.append((currentX, currentY))
        elif direction == 'L':
            for count in range(1, distance):
                currentX -= 1
                allLineCordinates.append((currentX, currentY))
        elif direction == 'U':
            for count in range(1, distance):
                currentY += 1
                allLineCordinates.append((currentX, currentY))
        elif direction == 'D':
            for count in range(1, distance):
                currentY -= 1
                allLineCordinates.append((currentX, currentY))
        else:
            print("Error, this should not happen.")

    return list(allLineCordinates)


def calculateShortestDistanceFromCentralPoint(line1Coord, line2Coord):
    intersections = set(line1Coord) & set(line2Coord)
    intersections.remove((0, 0))
    distancesFromCentralPoint = [abs(coord[0]) + abs(coord[1]) for coord in intersections]
    return min(distancesFromCentralPoint)


line1Coord = calculateLineCoordinates(line1)
line2Coord = calculateLineCoordinates(line2)

minDist1 = calculateShortestDistanceFromCentralPoint(line1Coord, line2Coord)
print(minDist1)


def calculateShortestAmountOfStepsFromCentralPoint(line1Coord, line2Coord):
    intersections = set(line1Coord) & set(line2Coord)
    intersections.remove((0, 0))
    currentMinDist = math.inf
    for coord in intersections:
        minDist = line1Coord.index(coord) + line2Coord.index(coord)
        if minDist < currentMinDist:
            currentMinDist = minDist
    return currentMinDist


minDist2 = calculateShortestAmountOfStepsFromCentralPoint(line1Coord, line2Coord)
print(minDist2)
