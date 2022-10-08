from typing import List

file = open("Day3Input1", "r")

if file.mode == "r":
    weights: List[int] = list(map(int, file.read().splitlines()))


def calculateFuelFromWeight(weight):
    return int(weight / 3) - 2


def calculateFuelForWeightAndAllFuelWeightToo(weight):
    sumFuel = 0
    currentWeightThatNeedsFuel = weight
    while True:
        currentFuelNeeded = calculateFuelFromWeight(currentWeightThatNeedsFuel)
        if currentFuelNeeded >= 0:
            sumFuel += currentFuelNeeded
            currentWeightThatNeedsFuel = currentFuelNeeded
        else:
            break
    return sumFuel


sumFuel = 0
for weight in weights:
    sumFuel += calculateFuelFromWeight(weight)

print(sumFuel)
print(calculateFuelFromWeight(1969))
print(calculateFuelFromWeight(100756))
print()
print(calculateFuelForWeightAndAllFuelWeightToo(14))
print(calculateFuelForWeightAndAllFuelWeightToo(1969))
print(calculateFuelForWeightAndAllFuelWeightToo(100756))

sumFuelAllModules = 0
for weight in weights:
    sumFuelAllModules += calculateFuelForWeightAndAllFuelWeightToo(weight)

print(sumFuelAllModules)
