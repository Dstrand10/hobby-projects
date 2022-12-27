import re
import sympy


def func1(monkeyOperations, monkey, part1):
    root_monkey = monkeyOperations[monkey]
    while re.search('[a-zA-Z]', root_monkey):
        tmp_root_monkey = ''
        for word in root_monkey.split(" "):
            if not part1 and (word == 'humn' or word == 'å'):
                tmp_root_monkey += " å"
            elif re.search('[a-zA-Z]', word):
                tmp_root_monkey += " ( " + monkeyOperations[word] + " )"
            else:
                tmp_root_monkey += " " + word
        root_monkey = tmp_root_monkey
    return root_monkey.replace(" ", "")


def func2(monkeyoperations):
    firstNbr, _, secondNbr = monkeyoperations['root'].split()
    firstEq = func1(monkeyoperations, firstNbr, False)
    secondEq = func1(monkeyoperations, secondNbr, False)
    return sympy.solve(firstEq + "-(" + secondEq + ")", sympy.Symbol('å'))[0]

    # secondEq = eval(func1(monkeyoperations, secondNbr, False))
    # z_increasing = eval(firstEq.replace('å', '2')) > eval(firstEq.replace('å', '1'))
    # z_low = 0
    # z_high = int(1e20)
    # while z_low != z_high:
    #     mid = z_low + (z_high - z_low) // 2
    #     firstEqZinserted = eval(firstEq.replace('å', str(mid)))
    #     if firstEqZinserted == secondEq:
    #         return mid
    #     elif (firstEqZinserted > secondEq and z_increasing) or (firstEqZinserted < secondEq and not z_increasing):
    #         z_high = mid
    #     else:
    #         z_low = mid


def main():
    monkeyOperations = dict()
    for line in open("input.txt").read().split("\n"):
        monkeyOperations[line.split(": ")[0]] = line.split(": ")[1]

    sol1 = int(eval(func1(monkeyOperations, 'root', True)))
    print(f"Solution 1: ", sol1)

    sol2 = func2(monkeyOperations)
    print(f"Solution 2: ", sol2)


if __name__ == "__main__":
    main()
