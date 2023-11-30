class Intcode:

    def __init__(self):
        self.index = 0
        self.memory = None
        self.inputSignals = []
        self.latestPrint = None
        self.relativeBase = 0
        self.printModeOn = True
        self.returnMode = not self.printModeOn

    def setInputSignals(self, inputSignals):
        for inputsignal in inputSignals:
            self.inputSignals.append(inputsignal)
        return self

    def setMemory(self, memory):
        self.memory = {k: v for k, v in enumerate(memory)}
        return self

    def readCode(self, intCode):
        self.memory = intCode
        self.readCode()

    def setPrintModeOn(self):
        self.printModeOn = True
        self.returnMode = False
        return self

    def setReturnModeOn(self):
        self.printModeOn = False
        self.returnMode = True
        return self


    def readCode(self):
        stop = False
        DEFAULT_VALUE = 0
        iter = 1
        while not stop:
            iter += 1
            opCode, param1, param2, param3 = self.getCommand(self.memory[self.index])

            # Addition
            if opCode == 1:
                self.memory[self.parameterMode(param3, self.index + 3)] = self.memory.get(self.parameterMode(param1,
                                                                                                         self.index + 1), DEFAULT_VALUE) + \
                                                                          self.memory.get(self.parameterMode(param2,
                                                                                                         self.index + 2), DEFAULT_VALUE)
                self.index += 4

            # Multiplication
            elif opCode == 2:
                self.memory[self.parameterMode(param3, self.index + 3)] = self.memory.get(self.parameterMode(param1,
                                                                                                         self.index + 1), DEFAULT_VALUE) * \
                                                                          self.memory.get(self.parameterMode(param2,
                                                                                                         self.index + 2), DEFAULT_VALUE)
                self.index += 4

            # Get prompt
            elif opCode == 3:
                if len(self.inputSignals) > 0:
                    self.memory[self.parameterMode(param1, self.index + 1)] = self.inputSignals.pop(0)
                else:
                    self.memory[self.parameterMode(param1, self.index + 1)] = int(self.getInput())
                self.index += 2

            # Print output
            elif opCode == 4:
                self.latestPrint = self.memory. get(self.parameterMode(param1, self.index + 1), DEFAULT_VALUE)
                self.index += 2
                if self.printModeOn:
                    print(self.latestPrint)
                elif self.returnMode:
                    return self.latestPrint

            # Jump-if-True
            elif opCode == 5:
                if self.memory[self.parameterMode(param1, self.index + 1)] != 0:
                    self.index = self.memory[self.parameterMode(param2, self.index + 2)]
                else:
                    self.index += 3

            # Jump-if-False
            elif opCode == 6:
                if self.memory[self.parameterMode(param1, self.index + 1)] == 0:
                    self.index = self.memory[self.parameterMode(param2, self.index + 2)]
                else:
                    self.index += 3

            # Less than
            elif opCode == 7:
                if self.memory[self.parameterMode(param1, self.index + 1)] < self.memory[
                    self.parameterMode(param2, self.index + 2)]:
                    self.memory[self.parameterMode(param3, self.index + 3)] = 1
                else:
                    self.memory[self.parameterMode(param3, self.index + 3)] = 0
                self.index += 4

            # Equals
            elif opCode == 8:
                if self.memory[self.parameterMode(param1, self.index + 1)] == self.memory[
                    self.parameterMode(param2, self.index + 2)]:
                    self.memory[self.parameterMode(param3, self.index + 3)] = 1
                else:
                    self.memory[self.parameterMode(param3, self.index + 3)] = 0
                self.index += 4

            # Set relative base
            elif opCode == 9:
                self.relativeBase += self.memory[self.parameterMode(param1, self.index + 1)]
                self.index += 2

            # End program
            elif opCode == 99:
                stop = True
        return "SHOULD STOP"

    def getCommand(self, command):
        commandlist = list()
        commandlist.append(command % 100)
        command -= command % 100
        commandlist.append(int((command % 1000) / 100))
        command -= command % 1000
        commandlist.append(int((command % 10000) / 1000))
        command -= command % 10000
        commandlist.append(int((command % 100000) / 10000))
        command -= command % 100000
        return commandlist

    def parameterMode(self, param, idx):
        if param == 0:
            return self.memory[idx]
        elif param == 1:
            return idx
        elif param == 2:
            return self.relativeBase + self.memory[idx]

    def getInput(self):
        nbr = input("Enter number:")
        if type(nbr) is not int:
            EOFError("Error, not a valid input")
        return nbr
