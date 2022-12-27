def func1(data):
    X = 1
    addings = []
    X_values = []
    cnt = 0

    while True:
        if not data:
            break
        cnt += 1
        row = data.pop(0)
        if row.split()[0] == "addx":
            addings.append((int(row.split()[1]), 1))
        if cnt % 40 == 20:
            X_values.append(cnt * X)
        new_addings = []
        for add in addings.copy():
            if add[1] == 0:
                X += add[0]
            else:
                new_addings.append((add[0], add[1] - 1))
        addings = new_addings
        if row.split()[0] == "addx":
            cnt += 1
            if cnt == 220:
                print("Hej")
            if cnt % 40 == 20:
                X_values.append(cnt * X)
            new_addings = []
            for add in addings.copy():
                if add[1] == 0:
                    X += add[0]
                else:
                    new_addings.append((add[0], add[1] - 1))
            addings = new_addings
    print(X_values)
    return sum(X_values)


def func2(data):
    X = 1
    addings = []
    cnt = 0
    row_count = 0
    CRT = [[], [], [], [], [], [], [], []]
    while True:
        if not data:
            break
        if X - 1 <= cnt <= X + 1:
            CRT[row_count].append("#")
        else:
            CRT[row_count].append(".")
        cnt += 1
        row = data.pop(0)
        if row.split()[0] == "addx":
            addings.append((int(row.split()[1]), 1))
        if cnt % 40 == 0:
            row_count += 1
            cnt = 0
        new_addings = []
        for add in addings.copy():
            if add[1] == 0:
                X += add[0]
            else:
                new_addings.append((add[0], add[1] - 1))
        addings = new_addings
        if row.split()[0] == "addx":
            if X - 1 <= cnt <= X + 1:
                CRT[row_count].append("#")
            else:
                CRT[row_count].append(".")
            cnt += 1
            if cnt % 40 == 0:
                row_count += 1
                cnt = 0
            new_addings = []
            for add in addings.copy():
                if add[1] == 0:
                    X += add[0]
                else:
                    new_addings.append((add[0], add[1] - 1))
            addings = new_addings
    return CRT


def main():
    data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    # data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    data = [line.strip() for line in open("input.txt").readlines()]
    sol2 = func2(data)
    print(f"Solution 2: (EFUGLPAP)")
    for row in sol2:
        print(''.join(row))


if __name__ == "__main__":
    main()
