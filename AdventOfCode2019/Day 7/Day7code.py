from itertools import permutations
from Day5.Day5code import readIntCode


def returnAllPermutationsOfList(phases):
    return permutations(phases)


def runOneLoopAmplifiers(phaseGroup, startInput):
    inputToAmp = startInput
    for phase in phaseGroup:
        while True:
            inputs = [phase, inputToAmp]  # First the phase as input, then previous amp output as input
        print(inputs)
        print(intCode)
        ampMemoryInfo = readIntCode(intCode, inputs)
        inputToAmp = lastAmpOutput
    return lastAmpOutput


####################### Program run code ##################################
# file = open("Day7input", "r")
# content = file.read()
#
# possiblePhaseGroups = returnAllPermutationsOfList([0, 1, 2, 3, 4])
# possiblePhaseGroupsTest = [[5, 6, 7, 8, 9]]
#
# phaseAtMaxThruster = []
# maxThruster = 0
#
# for possiblePhaseGroup in possiblePhaseGroups:
#     intCode = list(map(int, content.split(",")))
#     print("This phase is " + str(possiblePhaseGroup))
#     startInputOnlyOneLoop = 0  # Starting with 0
#     lastOutput = runOneLoopAmplifiers(possiblePhaseGroup, startInputOnlyOneLoop)
#     print(lastOutput)
#     if lastOutput > maxThruster:
#         maxThruster = lastOutput
#         phaseAtMaxThruster = possiblePhaseGroup
#
# print()
# print(phaseAtMaxThruster)
# print(maxThruster)


################## PART 2 ###############################################################################################
file = open("Day7inputPart2Test", "r")
content = file.read()
intCode = list(map(int, content.split(",")))

possiblePhaseGroupsFeedback = returnAllPermutationsOfList([5, 6, 7, 8, 9])
possiblePhaseGroupsTest = [[9, 7, 8, 5, 6]]

maxThrusterFeedbackPhase = []
maxThrusterFeedback = 0

# amp class = [intCode, opCode, latestOutput, indexTracker]


for possiblePhaseGroup in possiblePhaseGroupsFeedback:
    print("This phase is " + str(possiblePhaseGroup))
    ampA = [intCode[:], 4, 0, 0]
    ampB = [intCode[:], 4, 0, 0]
    ampC = [intCode[:], 4, 0, 0]
    ampD = [intCode[:], 4, 0, 0]
    ampE = [intCode[:], 4, 0, 0]

    amps = [ampA, ampB, ampC, ampD, ampE]
    latestOutput = 0  # Starting with 0
    iteration = 0
    operationCode = 4
    while True:
        currentIter = iteration % 5
        currentAmp = amps[currentIter]
        if currentAmp[1] == 4:
            if iteration < 5:
                inputs = [possiblePhaseGroup[iteration], latestOutput]
            else:
                inputs = [latestOutput]
            print(currentAmp[0])
            print(inputs)
            amps[currentIter] = readIntCode(currentAmp[0], inputs, currentAmp[3])
            print("Printing Amps")
            print(amps)
        elif currentAmp[1] == 99:
            print("Finished")
            print(currentAmp[2])
            break
        latestOutput = amps[currentIter][2]
        iteration += 1
        if latestOutput > maxThrusterFeedback:
            maxThrusterFeedback = latestOutput
            maxThrusterFeedbackPhase = possiblePhaseGroup

print()
print(maxThrusterFeedbackPhase)
print(maxThrusterFeedback)
