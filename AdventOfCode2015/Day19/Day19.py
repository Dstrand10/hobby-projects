from random import shuffle

def iterateMolecule(molecule, rules):
    newMolecules = set()
    for (key, val) in rules:
        keyIdx = 0
        while key in molecule[keyIdx:]:
            tmp_molecule = molecule[keyIdx:]
            currIdx = keyIdx + tmp_molecule.index(key)
            newMolecules.add(molecule[:currIdx] + val + molecule[currIdx + len(key):])
            keyIdx = currIdx + len(key)
    return list(newMolecules)


with open("input.txt") as f:
    rules = list()
    for datarow in f.readlines():
        if "=>" in datarow:
            rules.append((datarow.split(" => ")[0], datarow.split(" => ")[1].replace("\n", "")))
        elif "=>" not in datarow and datarow != "\n":
            molecule = datarow
    print("Answer 1: " + str(len(iterateMolecule(molecule, rules))))

    rules_reversed = [(rule[-1], rule[0]) for rule in rules]
    cnt = 0
    medicine = molecule
    while medicine != "e":
        tmp_med = medicine
        for (val, key) in rules_reversed:
            if val in medicine:
                medicine = medicine.replace(val, key, 1)
                cnt += 1
                break
        if tmp_med == medicine:
            medicine = molecule
            shuffle(rules_reversed)
            cnt = 0
    print("Answer 2: " + str(cnt))
