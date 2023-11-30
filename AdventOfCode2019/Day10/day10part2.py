import numpy as np
from collections import defaultdict

file = open("Day10input", "r")
content = file.read()
asteroidMap = content.split("\n")

asteroidCords = []

yCount = 0
for row in asteroidMap:
    xCount = 0
    for place in row:
        if row[xCount] == "#":
            asteroidCords.append((xCount, yCount))
        xCount += 1
    yCount -= 1

chosenX = 14
chosenY = -17
asteroidCords.remove((chosenX, chosenY))

asteroidsRight = defaultdict(list)
asteroidsLeft = defaultdict(list)

for asteroid in asteroidCords:
    astX = asteroid[0]
    astY = asteroid[1]
    if astX == chosenX:
        if astY > chosenY:
            k = np.inf
            dist = np.abs(astY - chosenY)
            l1 = asteroidsRight[k]
            l1.append((dist, asteroid))
            l1.sort(key=lambda x: x[0])
            asteroidsRight[k] = l1
        else:
            k = -np.inf
            dist = np.abs(astY - chosenY)
            l1 = asteroidsLeft[k]
            l1.append((dist, asteroid))
            l1.sort(key=lambda x: x[0])
            asteroidsLeft[k] = l1
        continue
    elif astX > chosenX:
        k = (astY - chosenY) / (astX - chosenX)
        dist = np.sqrt(np.square(astY - chosenY) + np.square(astX - chosenX))
        l1 = asteroidsRight[k]
        l1.append((dist, asteroid))
        l1.sort(key=lambda x: x[0])
        asteroidsRight[k] = l1
    else:
        k = (astY - chosenY) / (astX - chosenX)
        dist = np.sqrt(np.square(astY - chosenY) + np.square(astX - chosenX))
        l1 = asteroidsLeft[k]
        l1.append((dist, asteroid))
        l1.sort(key=lambda x: x[0])
        asteroidsLeft[k] = l1
righty = list(asteroidsRight)
righty.sort(reverse=True)
lefty = list(asteroidsLeft)
lefty.sort(reverse=True)

cnt = 0
while cnt < 200:
    for k1 in righty:
        l_temp = asteroidsRight[k1]
        if len(l_temp) > 0:
            ast = l_temp.pop(0)[1]
            cnt += 1
        else:
            continue
        if cnt == 199:
            print(ast[0] * 100 + -1 * ast[1])

    for k2 in lefty:
        l_temp = asteroidsLeft[k2]
        if len(l_temp) > 0:
            ast = l_temp.pop(0)[1]
            cnt += 1
        else:
            continue
        if cnt == 199:
            print(ast[0] * 100 + -1 * ast[1])
