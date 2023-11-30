import numpy as np

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



