def func1(in_data):
    gamma = ""
    epsilon = ""
    for pos in range(len(in_data[0])):
        pos_sum = 0
        for row in in_data:
            pos_sum += int(row[pos])
        if pos_sum >= len(in_data)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon


def func2(in_data):
    oxygen = in_data.copy()
    co2 = in_data.copy()
    pos = 0
    while True:
        gamma, _ = func1(oxygen)
        _, epsilon = func1(co2)
        if len(oxygen) > 1:
            oxygen = [num for num in oxygen if num[pos] == gamma[pos]]
        if len(co2) > 1:
            co2 = [num for num in co2 if num[pos] == epsilon[pos]]
        if len(oxygen) == 1 and len(co2) == 1:
            break
        pos += 1
    return oxygen[0], co2[0]


def main():
    with open('input.txt') as f:
        in_data = list(map(str, f))
        rez = []

        for x in in_data:
            rez.append(x.replace("\n", ""))

        sol1_a, sol1_b = func1(rez)
        print(f"Solution 1: {int(sol1_a, 2) * int(sol1_b, 2)}")

        sol2_oxygen, sol2_co2 = func2(rez)
        print(f"Solution 2: {int(sol2_oxygen, 2) * int(sol2_co2, 2)}")


if __name__ == "__main__":
    main()
