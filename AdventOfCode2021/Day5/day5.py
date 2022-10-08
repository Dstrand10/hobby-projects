class ThermalLine:

    def __init__(self, in_data):
        coords = in_data.split(" -> ")
        self.x1 = int(coords[0].split(",")[0])
        self.y1 = int(coords[0].split(",")[1])
        self.x2 = int(coords[1].split(",")[0])
        self.y2 = int(coords[1].split(",")[1])

        self.isVertical = self.x1 == self.x2
        self.k = self.getK()
        self.m = self.getM()
        self.thermalPoints = self.getThermalPoints()

    def getK(self):
        if self.isVertical:
            return None
        else:
            return (self.y2 - self.y1) / (self.x2 - self.x1)

    def getM(self):
        if self.isVertical:
            return None
        else:
            return self.y1 - self.k * self.x1

    def getThermalPoints(self):
        thermalPoints = []
        if self.isVertical:
            for i in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                thermalPoints.append((self.x1, i))
            return thermalPoints

        if self.x1 < self.x2:
            for i in range(self.x1, self.x2 + 1):
                y = self.k * i + self.m
                if y.is_integer():
                    thermalPoints.append((i, int(y)))
        elif self.x2 < self.x1:
            for i in range(self.x2, self.x1 + 1):
                y = self.k * i + self.m
                if y.is_integer():
                    thermalPoints.append((i, int(y)))
        return thermalPoints


def func1(thermalLines):
    consideredThermalLines = [x for x in thermalLines if x.isVertical or x.k == 0]

    hotSpots = {}
    for thermalLine in consideredThermalLines:
        for coord in thermalLine.thermalPoints:
            hotSpots[coord] = hotSpots.get(coord, 0) + 1

    hotHotSpots = []
    for key, value in hotSpots.items():
        if value > 1:
            hotHotSpots.append((key, value))
    return len(hotHotSpots)



def func2(thermalLines):
    consideredThermalLines = thermalLines

    hotSpots = {}
    for thermalLine in consideredThermalLines:
        for coord in thermalLine.thermalPoints:
            hotSpots[coord] = hotSpots.get(coord, 0) + 1

    hotHotSpots = []
    for key, value in hotSpots.items():
        if value > 1:
            hotHotSpots.append((key, value))
    return len(hotHotSpots)


def main():
    with open('input.txt') as f:
        in_data = f.read().split("\n")

        thermalLines = []
        for row in in_data:
            thermalLines.append(ThermalLine(row))


        sol1 = func1(thermalLines)
        print(f"Solution 1: {sol1}")

        sol2 = func2(thermalLines)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
