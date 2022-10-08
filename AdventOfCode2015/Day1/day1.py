with open("input.txt") as f:
    floor = 0
    positionBasementVisited = None
    for idx, char in enumerate(f.read()):
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1 and positionBasementVisited is None:
            positionBasementVisited = idx + 1
    print("Answer 1: " + str(floor))
    print("Answer 2: " + str(positionBasementVisited))
