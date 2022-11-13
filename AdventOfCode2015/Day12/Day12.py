import json


def calculateTotSum(iterable, type):
    global totalSum
    global part
    if part == "part2" and type == "dict" and "red" in iterable.values():
        return
    if type in ["json", "list"]:
        for elem in iterable:
            if isinstance(elem, list):
                calculateTotSum(elem, "list")
            elif isinstance(elem, dict):
                calculateTotSum(elem, "dict")
            elif isinstance(elem, int):
                totalSum += elem
    elif type == "dict":
        for key, value in iterable.items():
            if isinstance(value, list):
                calculateTotSum(value, "list")
            elif isinstance(value, dict):
                calculateTotSum(value, "dict")
            elif isinstance(value, int):
                totalSum += value

            if isinstance(key, int):
                totalSum += value


with open("input.txt") as f:
    data = f.readline()
    jsonLoaded = json.loads(data)

    # Part 1
    totalSum = 0
    part = "part1"
    calculateTotSum(jsonLoaded, "json")
    print("Answer 1: " + str(totalSum))

    # Part 2
    totalSum = 0
    part = "part2"
    calculateTotSum(jsonLoaded, "json")
    print("Answer 2: " + str(totalSum))
