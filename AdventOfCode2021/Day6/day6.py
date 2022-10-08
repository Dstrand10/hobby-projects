def func(fish_timers, days):
    fish = [fish_timers.count(i) for i in range(9)]
    for day in range(days):
        fish_0 = fish.pop(0)
        fish[6] += fish_0
        fish.append(fish_0)
    return sum(fish)


def main():
    with open('input.txt') as f:
        in_data = list(map(int, f.read().split(",")))

        sol1 = func(in_data, 80)
        print(f"Solution 1: {sol1}")

        sol2 = func(in_data, 256)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
