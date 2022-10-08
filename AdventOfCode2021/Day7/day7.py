from collections import defaultdict


def func1(in_data):
    fuel_cost = []
    for i in range(min(in_data), max(in_data) + 1):
        cost = 0
        for crab_x in in_data:
            cost += abs(i - crab_x)
        fuel_cost.append(cost)

    return min(fuel_cost)


def func2(in_data):
    fuel_cost = []
    cost_dict = defaultdict(int)

    inc_fuel_cost = 0
    for i in range(min(in_data), max(in_data) + 1):
        cost_dict[i] = inc_fuel_cost + cost_dict[i - 1]
        inc_fuel_cost += 1

    for i in range(min(in_data), max(in_data) + 1):
        cost = 0
        for crab_x in in_data:
            cost += cost_dict[abs(i - crab_x)]
        fuel_cost.append(cost)

    return min(fuel_cost)


def main():
    with open('input.txt') as f:
        in_data = list(map(int, f.read().split(",")))

        sol1 = func1(in_data)
        print(f"Solution 1: {sol1}")

        sol2 = func2(in_data)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
