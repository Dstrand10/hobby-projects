from Intcode import Intcode


class PaintingRobot:

    def __init__(self, data_input):
        self.coord_x = 0
        self.coord_y = 0
        self.dir = 0  # Pointing upwards
        self.intcodeBrain = Intcode().setMemory(data_input).setReturnModeOn()

    def setInputSignals(self, signal):
        self.intcodeBrain.inputSignals.append(signal)

    def readCode(self):
        output1 = self.intcodeBrain.readCode()
        output2 = self.intcodeBrain.readCode()
        if output1 == "SHOULD STOP" or output2 == "SHOULD STOP":
            return "SHOULD STOP"
        else:
            return [output1, output2]

    def updateDir(self, output):
        if output == 1:
            self.dir += 90
        elif output == 0:
            self.dir -= 90
        else:
            print("Error, shouldn't have come to this.")
        self.dir = self.dir % 360

    def walkForward(self):
        if self.dir == 0:
            self.coord_y += 1
        elif self.dir == 90:
            self.coord_x += 1
        elif self.dir == 180:
            self.coord_y -= 1
        elif self.dir == 270:
            self.coord_x -= 1
        else:
            print("Error, shouldn't have come to this.")


def paint(p_robot, hull_grid, was_ever_painted_grid):
    while True:
        current_panel_color = hull_grid.get((p_robot.coord_x, p_robot.coord_y), 0)
        p_robot.setInputSignals(current_panel_color)
        outputs = p_robot.readCode()

        if outputs == "SHOULD STOP":
            break

        if outputs[0] == 1:
            hull_grid[(p_robot.coord_x, p_robot.coord_y)] = 1
            was_ever_painted_grid[(p_robot.coord_x, p_robot.coord_y)] = 1
        elif outputs[0] == 0:
            hull_grid.pop((p_robot.coord_x, p_robot.coord_y), None)
        p_robot.updateDir(outputs[1])
        p_robot.walkForward()

    return hull_grid, was_ever_painted_grid


def drawHullGrid(painted_hull_grid):
    maxX, minX, maxY, minY = [0, 0, 0, 0]
    for key in painted_hull_grid.keys():
        if key[0] > maxX:
            maxX = key[0]
        elif key[0] < minX:
            minX = key[0]
        elif key[1] > maxY:
            maxY = key[1]
        elif key[1] < minY:
            minY = key[1]

    x = (maxX - minX) * "."
    matrix = []
    for i in range(maxY - minY + 1):
        matrix.append(x)

    for key in painted_hull_grid.keys():
        row = matrix[key[1] - minY]
        matrix[key[1] - minY] = row[:key[0] - minX] + "#" + row[key[0] - minX + 1:]

    for row in matrix[::-1]:
        print(row)


with open('input.txt') as f:
    input = list(map(int, f.read().split(",")))

    p_robot = PaintingRobot(input)
    was_ever_painted_grid = {}
    hull_grid = {}

    _, painted_was_ever_painted = paint(p_robot, hull_grid, was_ever_painted_grid)
    print("Solution 1: " + str(len(painted_was_ever_painted)))

    p_robot = PaintingRobot(input)
    was_ever_painted_grid = {}
    hull_grid = {(0, 0): 1}
    painted_hull_grid, b = paint(p_robot, hull_grid, was_ever_painted_grid)

    print("Solution 2:")
    drawHullGrid(painted_hull_grid)
