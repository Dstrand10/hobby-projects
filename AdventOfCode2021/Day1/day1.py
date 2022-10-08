def func1(in_data):
    count_increase = 0
    for i in range(len(in_data)):
        if in_data[i] - in_data[i - 1] > 0:
            count_increase += 1
    return count_increase


def func2(in_data, window_length):
    window_sum = []
    for i in range(len(in_data) - (window_length - 1)):
        window_sum.append(sum(in_data[i:i + window_length]))
    return func1(window_sum)


def main():
    with open('input.txt') as f:
        in_data = list(map(int, f))

        sol1 = func1(in_data)
        print(f"Solution 1: {sol1}")

        window_length = 110
        sol2 = func2(in_data, window_length)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
