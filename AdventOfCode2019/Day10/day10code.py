import numpy as np
import operator


file = open("Day10input", "r")
content = file.read()
asteroidMap = content.split("\n")
print(asteroidMap)

asteroidCords = []

yCount = 0
for row in asteroidMap:
    xCount = 0
    for place in row:
        if row[xCount] == "#":
            asteroidCords.append((xCount, yCount))
        xCount += 1
    yCount -= 1

print(asteroidCords)

maxDetectedAsteroids = 0
maxAsteroid = None

for asteroidCord in asteroidCords:
    otherAsteroids = asteroidCords[:]
    otherAsteroids.remove(asteroidCord)

    linesSaved = []
    for otherAsteroid in otherAsteroids:

        if (asteroidCord[0] - otherAsteroid[0]) == 0:
            k = np.Inf
        else:
            k = (asteroidCord[1] - otherAsteroid[1]) / (asteroidCord[0] - otherAsteroid[0])

        if k == np.Inf:
            m = None
        else:
            m = asteroidCord[1] - k * asteroidCord[0]

        if asteroidCord[0] - otherAsteroid[0] < 0:
            relativeX = 'Right'
        elif asteroidCord[0] - otherAsteroid[0] > 0:
            relativeX = 'Left'
        else:
            relativeX = 'SameXcoord'

        if asteroidCord[1] - otherAsteroid[1] < 0:
            relativeY = 'Right'
        elif asteroidCord[1] - otherAsteroid[1] > 0:
            relativeY = 'Left'
        else:
            relativeY = 'SameYcoord'

        dist = np.sqrt(
            np.square((asteroidCord[0] - otherAsteroid[0])) + np.square((asteroidCord[1] - otherAsteroid[1])))

        if (k, m, relativeX, relativeY) not in linesSaved:
            linesSaved.append((k, m, relativeX, relativeY))

    print(asteroidCord)
    print(linesSaved)
    print(len(linesSaved))

    if len(linesSaved) > maxDetectedAsteroids:
        maxDetectedAsteroids = len(linesSaved)
        maxAsteroid = asteroidCord

print(maxAsteroid)
print(maxDetectedAsteroids)

chosenAsteroid = (14, -17)
asteroidCords.remove(chosenAsteroid)
otherAsteroidsInfo = []

for otherAsteroid in asteroidCords:

    if (chosenAsteroid[0] - otherAsteroid[0]) == 0:
        k = np.Inf
    else:
        k = (chosenAsteroid[1] - otherAsteroid[1]) / (chosenAsteroid[0] - otherAsteroid[0])

    if k == np.Inf:
        m = None
    else:
        m = chosenAsteroid[1] - k * chosenAsteroid[0]

    if chosenAsteroid[0] - otherAsteroid[0] < 0:
        relativeX = 'Right'
    elif chosenAsteroid[0] - otherAsteroid[0] > 0:
        relativeX = 'Left'
    else:
        relativeX = 'SameXcoord'

    if chosenAsteroid[1] - otherAsteroid[1] < 0:
        relativeY = 'Up'
    elif chosenAsteroid[1] - otherAsteroid[1] > 0:
        relativeY = 'Down'
    else:
        relativeY = 'SameYcoord'

    dist = np.sqrt(
        np.square((chosenAsteroid[0] - otherAsteroid[0])) + np.square((chosenAsteroid[1] - otherAsteroid[1])))

    # k, m, relativeX, reltiveY, Distance
    otherAsteroidsInfo.append((k, m, relativeX, relativeY, dist, otherAsteroid[0], otherAsteroid[1]))

otherAsteroidsInfo.sort()


def filterUpperLeft(astCords):
    if astCords[2] == 'Left' and astCords[3] == 'Up':
        return True
    else:
        return False


def filterUpperRight(astCords):
    if astCords[2] == 'Right' and astCords[3] == 'Up':
        return True
    else:
        return False


def filterDownRight(astCords):
    if astCords[2] == 'Right' and astCords[3] == 'Down':
        return True
    else:
        return False


def filterDownLeft(astCords):
    if astCords[2] == 'Left' and astCords[3] == 'Down':
        return True
    else:
        return False


def filterSameX(astCords):
    if astCords[2] == 'SameXcoord':
        return True
    else:
        return False


def filterSameY(astCords):
    if astCords[3] == 'SameYcoord':
        return True
    else:
        return False


upperLeftAsteroids = list(filter(filterUpperLeft, otherAsteroidsInfo))
upperRightAsteroids = list(filter(filterUpperRight, otherAsteroidsInfo))
downRightAsteroids = list(filter(filterDownRight, otherAsteroidsInfo))
downLeftAsteroids = list(filter(filterDownLeft, otherAsteroidsInfo))
sameRelativeX = list(filter(filterSameX, otherAsteroidsInfo))
sameRelativeY = list(filter(filterSameY, otherAsteroidsInfo))

upperRightAsteroids.sort(key=lambda it: (it[0], -it[4]), reverse=True) # k descending, dist ascending
downRightAsteroids.sort(key=lambda it: [it[0], -it[4]], reverse=True)
downLeftAsteroids.sort(key=lambda it: [it[0], -it[4]], reverse=True)
upperLeftAsteroids.sort(key=lambda it: [it[0], -it[4]], reverse=True)
sameRelativeX.sort(key=lambda tup: [tup[0], tup[4]], reverse=False)
sameRelativeY.sort(key=lambda tup: [tup[0], tup[4]], reverse=False)


print("Upper Right")
print(upperRightAsteroids)
print("Down Right")
print(downRightAsteroids)
print("Down Left")
print(downLeftAsteroids)
print("Upper Left")
print(upperLeftAsteroids)
print("Same X")
print(sameRelativeX)
print("Same Y")
print(sameRelativeY)

AsteroidAreas = [upperRightAsteroids, sameRelativeY,
                 downRightAsteroids, sameRelativeX,
                 downLeftAsteroids, sameRelativeY, upperLeftAsteroids, sameRelativeX]

lastAsteroid = None
countDestroyedAst = 0

countArea = 0
while countDestroyedAst < 200:
    k = None
    currentAsteroidArea = AsteroidAreas[countArea % 8]
    for asteroid in currentAsteroidArea:

        if asteroid[0] != k:
            countDestroyedAst += 1
            k = asteroid[0]
            lastAsteroid = asteroid
            currentAsteroidArea.remove(asteroid)
    countArea += 1

print(lastAsteroid)
