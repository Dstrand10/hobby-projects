from Test2019IntcodeDone2021.IntcodeFile import Intcode
import numpy as np

class ArcadeCabinet:

    def __init__(self, input):
        self.intcode = Intcode().setReturnModeOn().setMemory(input)
        self.drawingInstructions = self.runDrawingSoftware()
        self.tiles = self.paintTiles()

    def runDrawingSoftware(self):
        values = []
        value = None
        while value != "SHOULD STOP":
            value = self.intcode.readCode()
            if value != "SHOULD STOP":
                values.append(int(value))
        return values

    def paintTiles(self):
        instructions = list(zip(self.drawingInstructions[::3], self.drawingInstructions[1::3], self.drawingInstructions[2::3]))
        tile_matrix = np.empty((max([x[0] for x in instructions]) + 1, max([y[1] for y in instructions]) + 1))
        for x, y, tile_val in instructions:
            tile_matrix[x][y] = tile_val
        return tile_matrix




with open("input.txt") as f:
    input_data = list(map(int, f.read().split(",")))

    arcCab = ArcadeCabinet(input_data)
    print("Solution 1: " + str(np.count_nonzero(arcCab.tiles == 2)))
