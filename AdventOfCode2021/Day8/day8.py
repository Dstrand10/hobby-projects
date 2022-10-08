class SignalSystem:

    def __init__(self, in_data):
        self.nbrDict = {}

        self.nbrDict[1] = [''.join(sorted([x for x in in_data.split(" ") if len(x) == 2][0]))]
        self.nbrDict[4] = [''.join(sorted([x for x in in_data.split(" ") if len(x) == 4][0]))]
        self.nbrDict[7] = [''.join(sorted([x for x in in_data.split(" ") if len(x) == 3][0]))]
        self.nbrDict[8] = [''.join(sorted([x for x in in_data.split(" ") if len(x) == 7][0]))]

        theFives = []
        for nbrcomb in [x for x in in_data.split(" ") if len(x) == 5]:
            sorted_nbr_comb = ''.join(sorted(nbrcomb))
            if sorted_nbr_comb not in theFives:
                theFives.append(sorted_nbr_comb)
        self.nbrDict[2] = theFives.copy()
        self.nbrDict[3] = theFives.copy()
        self.nbrDict[5] = theFives.copy()

        theSixes = []
        for nbrcomb in [x for x in in_data.split(" ") if len(x) == 6]:
            sorted_nbr_comb = ''.join(sorted(nbrcomb))
            if sorted_nbr_comb not in theSixes:
                theSixes.append(sorted_nbr_comb)

        self.nbrDict[0] = theSixes.copy()
        self.nbrDict[6] = theSixes.copy()
        self.nbrDict[9] = theSixes.copy()

        self.find9()
        self.find0()
        self.find6()

        self.letterPos1 = self.findFirstLetter()
        self.letterPos2 = self.findSecondLetter()

        self.find3()
        self.find2()
        self.find5()

    def find0(self):

        theZeros = self.nbrDict[0]
        for possibleNbr in theZeros.copy():
            for char in self.nbrDict[1][0]:
                if char not in possibleNbr:
                    theZeros.remove(possibleNbr)
                    break

        for possibleNbr in theZeros.copy():
            for char in self.nbrDict[7][0]:
                if char not in possibleNbr:
                    theZeros.remove(possibleNbr)
                    break
        theZeros.remove(self.nbrDict[9][0])

    def find9(self):
        theNines = self.nbrDict[9]
        for possibleNbr in theNines.copy():
            for char in self.nbrDict[1][0]:
                if char not in possibleNbr:
                    theNines.remove(possibleNbr)
                    break

        for possibleNbr in theNines.copy():
            for char in self.nbrDict[7][0]:
                if char not in possibleNbr:
                    theNines.remove(possibleNbr)
                    break
        for possibleNbr in theNines.copy():
            for char in self.nbrDict[4][0]:
                if char not in possibleNbr:
                    theNines.remove(possibleNbr)
                    break

    def find6(self):
        self.nbrDict[6].remove(self.nbrDict[0][0])
        self.nbrDict[6].remove(self.nbrDict[9][0])

    def find3(self):
        theThrees = self.nbrDict[3]
        for possibleNbr in theThrees.copy():
            for char in self.nbrDict[1][0]:
                if char not in possibleNbr:
                    theThrees.remove(possibleNbr)
                    break

        for possibleNbr in theThrees.copy():
            for char in self.nbrDict[7][0]:
                if char not in possibleNbr:
                    theThrees.remove(possibleNbr)
                    break

    def find2(self):
        theTwos = self.nbrDict[2]
        theTwos.remove(self.nbrDict[3][0])

        for possibleNbr in theTwos:
            if self.letterPos2 not in possibleNbr:
                theTwos.remove(possibleNbr)
        for possibleNbr in theTwos.copy():
            shouldStop = False
            for char in self.nbrDict[1][0]:
                if char not in possibleNbr:
                    shouldStop = True
                    break
            if not shouldStop:
                theTwos.remove(possibleNbr)

        for possibleNbr in theTwos.copy():
            shouldStop = False
            for char in self.nbrDict[7][0]:
                if char not in possibleNbr:
                    shouldStop = True
                    break
            if not shouldStop:
                theTwos.remove(possibleNbr)

    def find5(self):
        theFives = self.nbrDict[5]
        theFives.remove(self.nbrDict[3][0])
        theFives.remove(self.nbrDict[2][0])
        for possibleNbr in theFives.copy():
            shouldStop = False
            for char in self.nbrDict[1][0]:
                if char not in possibleNbr:
                    shouldStop = True
                    break
            if not shouldStop:
                theFives.remove(possibleNbr)

        for possibleNbr in theFives.copy():
            shouldStop = False
            for char in self.nbrDict[7][0]:
                if char not in possibleNbr:
                    shouldStop = True
                    break
            if not shouldStop:
                theFives.remove(possibleNbr)

    def findFirstLetter(self):
        for letter in self.nbrDict[7][0]:
            if letter not in self.nbrDict[1][0]:
                return letter

    def findSecondLetter(self):
        for letter in self.nbrDict[1][0]:
            if letter not in self.nbrDict[6][0]:
                return letter

    def calculateOutput(self, row):
        output = row.split(" | ")[1]
        outputNbr = ""
        for nbr in output.split(" "):
            outputNbr += str(list(self.nbrDict.keys())[list(self.nbrDict.values()).index([''.join(sorted(nbr))])])
        return outputNbr


def func1(in_data):
    nbrs_appear = 0
    for row in in_data:
        output = row.split(" | ")[1]
        for signal in output.split(" "):
            if len(signal) in [2, 3, 4, 7]:
                nbrs_appear += 1

    return nbrs_appear



def func2(in_data):
    totSum = 0
    for row in in_data:
        signalSystem = SignalSystem(row)
        totSum += int(signalSystem.calculateOutput(row))
    return totSum

def main():
    with open('input.txt') as f:
        in_data = f.read().split("\n")

        sol1 = func1(in_data)
        print(f"Solution 1: {sol1}")

        sol2 = func2(in_data)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
