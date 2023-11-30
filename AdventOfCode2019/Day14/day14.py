from math import ceil


def calculate_ore(amount_fuel):
    data = open("day14input.txt").read().splitlines()

    needed = []
    result = []
    ing = {"ORE": 1}
    ing_plus = {"ORE": 0}

    for e in data:
        need, res = e.split(" => ")
        needed.append(need.split(", "))
        amount, ingr = res.split(" ")
        result.append(ingr)
        ing[ingr] = int(amount)
        ing_plus[ingr] = 0

    chain = ["FUEL"]
    chain_needed = [amount_fuel]
    chain_levelsdeep = [1]

    e = 0
    while e < len(chain):
        levelsdeep = chain_levelsdeep[e] + 1
        for res_what in result:
            if res_what == chain[e]:
                for g in reversed(needed[result.index(res_what)]):
                    need_amount, need_what = g.split(" ")
                    chain.insert(e + 1, need_what)
                    chain_needed.insert(e + 1, int(need_amount))
                    chain_levelsdeep.insert(e + 1, levelsdeep)
        e += 1

    ore_total = 0
    p = 1
    while p < len(chain):
        q = 0
        while q < p:
            if chain_levelsdeep[q] < chain_levelsdeep[p]:
                key = q
            q += 1
        if chain[p] != "ORE":
            amountneeded_raw = ((chain_needed[p]) * int(chain_needed[key] / ing[chain[key]])) - ing_plus[chain[p]]
            amountneeded = ceil(amountneeded_raw / ing[chain[p]]) * ing[chain[p]]
            chain_needed[p] = amountneeded
            ing_plus[chain[p]] = amountneeded - amountneeded_raw
        else:
            ore_total += chain_needed[p] * int(chain_needed[key] / ing[chain[key]])
        p += 1
    return ore_total

one_fuel = calculate_ore(1)
print(one_fuel)

# part 2: 1639374
print(int(int(1000000000000 / one_fuel) * (1000000000000 / calculate_ore(int(1000000000000 / one_fuel)))))

################################################################################################################################
# part 2 alternative:
triedfuels = []
tryfuel = int(1000000000000 / one_fuel)
a = 0
while a == False:
    tried = calculate_ore(tryfuel)
    if tried not in triedfuels:
        triedfuels.append(tried)
    elif tried <= 1000000000000 and tried in triedfuels:
        print(int(tryfuel))
        break
    test = 1000000000000 / tried
    tryfuel *= test