import re


def turnOffLight(lights, coord):
    lights.pop(coord, 0)


def turnOnLight(lights, coord):
    lights[coord] = 1


def updateLights(lights, cmd):
    commandType = cmd[0]
    coords = cmd[1]
    if commandType == "toggle":
        for xcoord in range(coords[0], coords[2] + 1):
            for ycoord in range(coords[1], coords[3] + 1):
                if (xcoord, ycoord) in lights.keys():
                    turnOffLight(lights, (xcoord, ycoord))
                else:
                    turnOnLight(lights, (xcoord, ycoord))
    elif commandType == "turn off":
        for xcoord in range(coords[0], coords[2] + 1):
            for ycoord in range(coords[1], coords[3] + 1):
                turnOffLight(lights, (xcoord, ycoord))
    elif commandType == "turn on":
        for xcoord in range(coords[0], coords[2] + 1):
            for ycoord in range(coords[1], coords[3] + 1):
                turnOnLight(lights, (xcoord, ycoord))
    else:
        EOFError


def turnBrightnessUp(lights2, coord, steps=1):
    lights2[coord] = lights2.get(coord, 0) + steps


def turnBrightnessDown(lights2, coord):
    if lights2.get(coord, 0) > 0:
        lights2[coord] = lights2[coord] - 1
    else:
        lights2.pop(coord, 0)


def updateLightBrightness(lights, commands):
    commandType = commands[0]
    coords = commands[1]
    if commandType == "toggle":
        for xcoord in range(coords[0], coords[2] + 1):
            for ycoord in range(coords[1], coords[3] + 1):
                turnBrightnessUp(lights, (xcoord, ycoord), 2)
    elif commandType == "turn off":
        for xcoord in range(coords[0], coords[2] + 1):
            for ycoord in range(coords[1], coords[3] + 1):
                turnBrightnessDown(lights, (xcoord, ycoord))
    elif commandType == "turn on":
        for xcoord in range(coords[0], coords[2] + 1):
            for ycoord in range(coords[1], coords[3] + 1):
                turnBrightnessUp(lights, (xcoord, ycoord))
    else:
        EOFError


with open("input.txt") as f:
    toggleCommands = []
    for line in f.readlines():
        toggleCommands.append((
            ' '.join(re.findall('([A-Za-z]+)', line)[:-1]),
            list(map(int, re.findall('(\d+)', line)))
        ))
    lightsOnOff = {}
    for toggleCommand in toggleCommands:
        updateLights(lightsOnOff, toggleCommand)
    print("Answer 1: " + str(len(lightsOnOff.keys())))

    lightsBrightness = {}
    for toggleCommand in toggleCommands:
        updateLightBrightness(lightsBrightness, toggleCommand)
    print("Answer 2: " + str(sum(lightsBrightness.values())))
