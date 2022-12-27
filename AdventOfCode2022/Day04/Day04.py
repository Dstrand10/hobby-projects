def func1(data):
    sum = 0
    for row in data:
        fl = int(row.split(",")[0].split("-")[0])
        fr = int(row.split(",")[0].split("-")[1])
        sl = int(row.split(",")[1].split("-")[0])
        sr = int(row.split(",")[1].split("-")[1])
        if (
                (fl <= sl and sr <= fr)
                or
                (sl <= fl and fr <= sr)
                ):
            sum += 1
    return sum


def func2(data):
    sum = 0
    for row in data:
        fl = int(row.split(",")[0].split("-")[0])
        fr = int(row.split(",")[0].split("-")[1])
        sl = int(row.split(",")[1].split("-")[0])
        sr = int(row.split(",")[1].split("-")[1])
        if (
                (fl <= sl <= fr)
                or
                (fl <= sr <= fr)
                or
                (sl <= fl <= sr)
                or
                (sl <= fr <= sr)):
            sum += 1
    return sum


def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
