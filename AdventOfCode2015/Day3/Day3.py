class presentDealer:
    def __init__(self):
        self.xcoord = 0
        self.ycoord = 0
        self.houses = {(self.xcoord, self.ycoord): 1}


def updatePresentDealer(pd, dir):
    if dir == "^":
        pd.ycoord += 1
    elif dir == ">":
        pd.xcoord += 1
    elif dir == "v":
        pd.ycoord -= 1
    else:
        pd.xcoord -= 1
    pd.houses[(pd.xcoord, pd.ycoord)] = pd.houses.get((pd.xcoord, pd.ycoord), 0) + 1


with open("input.txt") as f:
    input = f.read()
    santa = presentDealer()
    for dir in input:
        updatePresentDealer(santa, dir)
    print("Answer 1: " + str(len(santa.houses)))
    santa = presentDealer()
    robot = presentDealer()
    for idx, dir in enumerate(input):
        if idx % 2 == 0:
            updatePresentDealer(santa, dir)
        else:
            updatePresentDealer(robot, dir)
    print("Answer 2: " + str(len(set(list(santa.houses.keys()) + list(robot.houses.keys())))))
