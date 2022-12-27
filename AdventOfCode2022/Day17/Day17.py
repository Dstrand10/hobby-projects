import math
from collections import defaultdict


class Rock:
    def __init__(self):
        self.coords = set()

    def shiftCoords(self, dir):
        tmp_set = set()
        for coord in self.coords:
            new_coord = (coord[0] + dir[0], coord[1] + dir[1])
            if new_coord[0] == 0 or new_coord[0] == 8:
                return self.coords
            else:
                tmp_set.add(new_coord)
        return tmp_set

    def shiftCoordsLeft(self):
        return self.shiftCoords([-1, 0])

    def shiftCoordsRight(self):
        return self.shiftCoords([1, 0])

    def shiftCoordsDown(self):
        return self.shiftCoords([0, 1])


    def firstRock(self, mostBottomLeftCoord):
        self.coords = set()
        x = mostBottomLeftCoord[0]
        y = mostBottomLeftCoord[1]
        self.coords.add(mostBottomLeftCoord)
        self.coords.add((x + 1, y))
        self.coords.add((x + 2, y))
        self.coords.add((x + 3, y))

    def secondRock(self, mostBottomLeftCoord):
        self.coords = set()
        x = mostBottomLeftCoord[0]
        y = mostBottomLeftCoord[1]
        self.coords.add(mostBottomLeftCoord)
        self.coords.add((x - 1, y - 1))
        self.coords.add((x, y - 1))
        self.coords.add((x + 1, y - 1))
        self.coords.add((x, y - 2))

    def thirdRock(self, mostBottomLeftCoord):
        self.coords = set()
        x = mostBottomLeftCoord[0]
        y = mostBottomLeftCoord[1]
        self.coords.add(mostBottomLeftCoord)
        self.coords.add((x + 1, y))
        self.coords.add((x + 2, y))
        self.coords.add((x + 2, y - 1))
        self.coords.add((x + 2, y - 2))

    def fourthRock(self, mostBottomLeftCoord):
        self.coords = set()
        x = mostBottomLeftCoord[0]
        y = mostBottomLeftCoord[1]
        self.coords.add(mostBottomLeftCoord)
        self.coords.add((x, y - 1))
        self.coords.add((x, y - 2))
        self.coords.add((x, y - 3))

    def fifthRock(self, mostBottomLeftCoord):
        self.coords = set()
        x = mostBottomLeftCoord[0]
        y = mostBottomLeftCoord[1]
        self.coords.add(mostBottomLeftCoord)
        self.coords.add((x, y - 1))
        self.coords.add((x + 1, y))
        self.coords.add((x + 1, y - 1))


def playTetris(jetStream, cntJetStream, playingField, rock):
    while True:
        jet = jetStream[cntJetStream % len(jetStream)]
        rock_move_possible = True

        # Shift left/right
        if jet == '<':
            poss_coords = rock.shiftCoordsLeft()
        else:
            poss_coords = rock.shiftCoordsRight()
        #Only move if rock coords differ
        if not poss_coords == rock.coords:
            for poss_coord in poss_coords:
                if poss_coord in playingField.keys():
                    rock_move_possible = False
                    break
            if rock_move_possible:
                rock.coords = poss_coords
        cntJetStream += 1

        # Shift coords down
        rock_move_possible = True
        poss_coords_down = rock.shiftCoordsDown()
        for poss_coord_down in poss_coords_down:
            if poss_coord_down in playingField.keys():
                rock_move_possible = False
                break
        if rock_move_possible:
            rock.coords = poss_coords_down
        else:
            for coord in rock.coords:
                playingField[coord] = 1
            break
    return cntJetStream


def solve(jetStream):
    rock = Rock()
    cntJetStream = 0
    cntRock = 0
    playingField = defaultdict(int)
    haveJumped = False
    pattern = {}
    limit = 1000000000000
    for i in range(9):
        playingField[(i, 0)] = 1

    while True:
        if cntRock == 2022:
            part1 = -min([k[1] for k, v in playingField.items()])
        if cntRock == limit:
            part2 = -min([k[1] for k, v in playingField.items()]) - skipAheadAmount
            break
        top_y = min([k[1] for k, _ in playingField.items()])
        if cntRock % 5 == 0:
            rock.firstRock((3, top_y - 4))
        elif cntRock % 5 == 1:
            rock.secondRock((4, top_y - 4))
        elif cntRock % 5 == 2:
            rock.thirdRock((3, top_y - 4))
        elif cntRock % 5 == 3:
            rock.fourthRock((3, top_y - 4))
        elif cntRock % 5 == 4:
            rock.fifthRock((3, top_y - 4))
        cntJetStream = playTetris(jetStream, cntJetStream, playingField, rock)

        # Signature
        signature = ((cntJetStream % len(jetStream), cntRock % 5, frozenset([(x, top_y - y) for (x, y) in playingField if top_y - y >= -10])))

        if signature in pattern and 2022 < cntRock and not haveJumped:
            oldCntRock, oldTopY = pattern[signature]
            deltaCntRock = cntRock - oldCntRock
            deltaTopY = top_y - oldTopY
            periodsPossible = math.floor((limit - cntRock) / deltaCntRock)
            skipAheadAmount = periodsPossible * deltaTopY
            cntRock += periodsPossible * deltaCntRock
            haveJumped = True

        pattern[signature] = (cntRock, top_y)

        cntRock += 1
    return part1, part2

def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read()
    # data = [row.split() for row in data]
    sol1, sol2 = solve(data)
    print(f"Solution 1: {sol1}")
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
