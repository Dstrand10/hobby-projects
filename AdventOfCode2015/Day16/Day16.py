import re


class Sue:
    def __init__(self, name, children=None, cats=None, samoyeds=None, pomeranians=None, akitas=None, vizslas=None,
                 goldfish=None, trees=None, cars=None, perfumes=None):
        self.name = name
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes


def addInfoToSue(sue: Sue, info, nbr):
    if info == "children":
        sue.children = nbr
    elif info == "cats":
        sue.cats = nbr
    elif info == "samoyeds":
        sue.samoyeds = nbr
    elif info == "pomeranians":
        sue.pomeranians = nbr
    elif info == "akitas":
        sue.akitas = nbr
    elif info == "vizslas":
        sue.vizslas = nbr
    elif info == "goldfish":
        sue.goldfish = nbr
    elif info == "trees":
        sue.trees = nbr
    elif info == "cars":
        sue.cars = nbr
    elif info == "perfumes":
        sue.perfumes = nbr


with open("input.txt") as f:
    sues = list()
    for datarow in f.readlines():
        datarow = datarow.replace("\n", "")
        current_sue = Sue(name=datarow.split(":")[0])
        for info in re.split(r'\d:', datarow)[1].split(","):
            addInfoToSue(current_sue, info.split(":")[0].replace(" ", ""), int(info.split(":")[1].replace(" ", "")))
        sues.append(current_sue)
    # children: 3
    # cats: 7
    # samoyeds: 2
    # pomeranians: 3
    # akitas: 0
    # vizslas: 0
    # goldfish: 5
    # trees: 3
    # cars: 2
    # perfumes: 1
    correct_sue = Sue(name="correct Sue", children=3, cats=7, samoyeds=2, pomeranians=3, akitas=0, vizslas=0,
                      goldfish=5, trees=3, cars=2,
                      perfumes=1)
    # Part 1
    filtered_sues_part1 = filter(lambda sue:
                                 (sue.children is None or sue.children == correct_sue.children)
                                 and
                                 (sue.cats is None or sue.cats == correct_sue.cats)
                                 and
                                 (sue.samoyeds is None or sue.samoyeds == correct_sue.samoyeds)
                                 and
                                 (sue.pomeranians is None or sue.pomeranians == correct_sue.pomeranians)
                                 and
                                 (sue.akitas is None or sue.akitas == correct_sue.akitas)
                                 and
                                 (sue.vizslas is None or sue.vizslas == correct_sue.vizslas)
                                 and
                                 (sue.goldfish is None or sue.goldfish == correct_sue.goldfish)
                                 and
                                 (sue.trees is None or sue.trees == correct_sue.trees)
                                 and
                                 (sue.cars is None or sue.cars == correct_sue.cars)
                                 and
                                 (sue.perfumes is None or sue.perfumes == correct_sue.perfumes),
                                 sues)
    for filtered_sue in filtered_sues_part1:
        print("Answer 1: " + str(filtered_sue.name).split(" ")[1])

    # Part 2
    filtered_sues_part1 = filter(lambda sue:
                                 (sue.children is None or sue.children == correct_sue.children)
                                 and
                                 (sue.cats is None or sue.cats > correct_sue.cats)
                                 and
                                 (sue.samoyeds is None or sue.samoyeds == correct_sue.samoyeds)
                                 and
                                 (sue.pomeranians is None or sue.pomeranians < correct_sue.pomeranians)
                                 and
                                 (sue.akitas is None or sue.akitas == correct_sue.akitas)
                                 and
                                 (sue.vizslas is None or sue.vizslas == correct_sue.vizslas)
                                 and
                                 (sue.goldfish is None or sue.goldfish < correct_sue.goldfish)
                                 and
                                 (sue.trees is None or sue.trees > correct_sue.trees)
                                 and
                                 (sue.cars is None or sue.cars == correct_sue.cars)
                                 and
                                 (sue.perfumes is None or sue.perfumes == correct_sue.perfumes),
                                 sues)
    for filtered_sue in filtered_sues_part1:
        print("Answer 2: " + str(filtered_sue.name).split(" ")[1])
