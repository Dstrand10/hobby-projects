def func1(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        firstCompartment = rucksack[:int(len(rucksack) / 2)]
        secondCompartment = rucksack[int(len(rucksack) / 2):]
        for item in firstCompartment:
            if item in secondCompartment:
                if item.islower():
                    sum += ord(item) - 96
                else:
                    sum += ord(item) - 38
                break
    return sum


def func2(rucksacks):
    sum = 0
    n = 3
    groupedElves = [rucksacks[i: i + n] for i in range(0, (len(rucksacks) - n + 1), n)]
    for group in groupedElves:
        elf1Badges = group[0]
        for badge in elf1Badges:
            if badge in group[1] and badge in group[2]:
                if badge.islower():
                    sum += ord(badge) - 96
                else:
                    sum += ord(badge) - 38
                break
    return sum


def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
