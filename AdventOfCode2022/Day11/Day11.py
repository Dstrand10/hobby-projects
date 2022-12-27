from functools import reduce


def test(item: int, divisible: int, firstMonkey: int, secondMonkey: int) -> int:
    return firstMonkey if item % divisible == 0 else secondMonkey


class Monkey:
    def __init__(self, items: list, increaseWorry, divisible: int, firstMonkey: int, secondMonkey: int):
        self.items = items
        self.increaseWorry = increaseWorry
        self.divisible = divisible
        self.test = lambda item: test(item, divisible, firstMonkey, secondMonkey)
        self.numberOfOperations = 0

    def doMonkeyStuff(self, item: int, Monkeys: list, moduloOperator: int = None):
        worry_level_item = self.increaseWorry(item)
        self.numberOfOperations += 1
        if moduloOperator is None:
            worry_level_item = worry_level_item // 3
        else:
            worry_level_item = worry_level_item % moduloOperator
        throw_to_monkey = self.test(worry_level_item)
        self.items.pop(0)
        Monkeys[throw_to_monkey].items.append(worry_level_item)


def func1(monkeys):
    for i in range(20):
        for monkey in monkeys:
            for item in monkey.items.copy():
                monkey.doMonkeyStuff(item, monkeys)

    nbrOperations = list(map(lambda x: x.numberOfOperations, monkeys))
    nbrOperations.sort()

    return nbrOperations[-1] * nbrOperations[-2]


def func2(monkeys):
    moduloOperator = reduce(lambda x, y: x * y, [monkey.divisible for monkey in monkeys])
    for i in range(10000):
        for monkey in monkeys:
            for item in monkey.items.copy():
                monkey.doMonkeyStuff(item, monkeys, moduloOperator)

    nbrOperations = list(map(lambda x: x.numberOfOperations, monkeys))
    nbrOperations.sort()

    return nbrOperations[-1] * nbrOperations[-2]


def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]
    monkeys = [
        Monkey([72, 97], lambda x: x * 13, 19, 5, 6),
        Monkey([55, 70, 90, 74, 95], lambda x: x * x, 7, 5, 0),
        Monkey([74, 97, 66, 57], lambda x: x + 6, 17, 1, 0),
        Monkey([86, 54, 53], lambda x: x + 2, 13, 1, 2),
        Monkey([50, 65, 78, 50, 62, 99], lambda x: x + 3, 11, 3, 7),
        Monkey([90], lambda x: x + 4, 2, 4, 6),
        Monkey([88, 92, 63, 94, 96, 82, 53, 53], lambda x: x + 8, 5, 4, 7),
        Monkey([70, 60, 71, 69, 77, 70, 98], lambda x: x * 7, 3, 2, 3)
    ]

    sol1 = func1(monkeys.copy())
    print(f"Solution 1: {sol1}")

    sol2 = func2(monkeys.copy())
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
