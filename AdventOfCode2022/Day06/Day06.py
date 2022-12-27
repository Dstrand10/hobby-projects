def func(data, length):
    for idx, char in enumerate(data):
        if len(set(data[idx:idx+length])) == length:
            return idx + length

def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    data = open("input.txt").read()
    # data = open("input.txt").read().split("\n")[0]
    # data = [row.split() for row in data]
    print(data)

    sol1 = func(data, 4)
    print(f"Solution 1: {sol1}")

    sol2 = func(data, 14)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
