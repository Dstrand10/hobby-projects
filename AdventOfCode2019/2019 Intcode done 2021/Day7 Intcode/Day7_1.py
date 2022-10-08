import itertools

from Intcode import Intcode

input = list(map(int, open("inputdata_1", "r").readline().split(",")))


def problem1(input):
    greatestThrust = 0
    bestPhase = None
    phasesParams = "01234"
    phases = list(itertools.permutations(phasesParams, 5))

    for phase in phases:
        output = 0
        for param in phase:
            output = Intcode().setInputSignals([int(param), output]).setMemory(input.copy()).readCode()
        if output > greatestThrust:
            bestPhase = phase
            greatestThrust = output
    print(bestPhase)
    print(greatestThrust)


problem1(input)


def problem2(input):
    greatestThrust = 0
    greatestPhase = []
    phasesParams = "56789"
    phases = list(itertools.permutations(phasesParams, 5))

    for phase in phases:
        output = 0
        AmpA = Intcode().setMemory(input.copy())
        AmpB = Intcode().setMemory(input.copy())
        AmpC = Intcode().setMemory(input.copy())
        AmpD = Intcode().setMemory(input.copy())
        AmpE = Intcode().setMemory(input.copy())
        output = AmpA.setInputSignals([int(phase[0]), output]).readCode()
        output = AmpB.setInputSignals([int(phase[1]), output]).readCode()
        output = AmpC.setInputSignals([int(phase[2]), output]).readCode()
        output = AmpD.setInputSignals([int(phase[3]), output]).readCode()
        output = AmpE.setInputSignals([int(phase[4]), output]).readCode()
        while True:
            lastOutput = output
            output = AmpA.setInputSignals([output]).readCode()
            output = AmpB.setInputSignals([output]).readCode()
            output = AmpC.setInputSignals([output]).readCode()
            output = AmpD.setInputSignals([output]).readCode()
            output = AmpE.setInputSignals([output]).readCode()
            if output == lastOutput:
                if output > greatestThrust:
                    greatestPhase = phase
                    greatestThrust = output
                break

    print(greatestPhase)
    print(greatestThrust)


problem2(input)
