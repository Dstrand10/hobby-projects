def test(item, divisible, firstMonkey, secondMonkey):
    return firstMonkey if item % divisible == 0 else secondMonkey

class Monkey:

    def __init__(self, items: list, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.numberOfOperations = 0

    def doMonkeyStuff(self, item, Monkeys: list):
        # Inspect
        worry_level_item = self.operation(item)
        self.numberOfOperations += 1
        # Bored with item
        worry_level_item = worry_level_item // 3
        throw_to_monkey = self.test(worry_level_item)
        self.items.pop(0)
        Monkeys[throw_to_monkey].items.append(worry_level_item)




def func1(data):
    monkeys =[
        Monkey([72, 97], lambda x: x * 13, lambda y: test(y, 19, 5, 6)),
        Monkey([55, 70, 90, 74, 95], lambda x: x * x, lambda y: test(y, 7, 5, 0)),
        Monkey([74, 97, 66, 57], lambda x: x + 6, lambda y: test(y, 17, 1, 0)),
        Monkey([86, 54, 53], lambda x: x + 2, lambda y: test(y, 13, 1, 2)),
        Monkey([50, 65, 78, 50, 62, 99], lambda x: x + 3, lambda y: test(y, 11, 3, 7)),
        Monkey([90], lambda x: x + 4, lambda y: test(y, 2, 4, 6)),
        Monkey([88, 92, 63, 94, 96, 82, 53, 53], lambda x: x + 8, lambda y: test(y, 5, 4, 7)),
        Monkey([70, 60, 71, 69, 77, 70, 98], lambda x: x * 8, lambda y: test(y, 3, 2, 3))
    ]

    for i in range(20):
        for monkey in monkeys:
            for item in monkey.items.copy():
                monkey.doMonkeyStuff(item, monkeys)


    for monkey in monkeys:
        print(monkey.numberOfOperations)

    return None


def func2(data):
    return None


def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")

if __name__ == "__main__":
    main()
