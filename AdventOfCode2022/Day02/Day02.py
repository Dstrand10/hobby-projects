def func1(data):
    score = 0
    for rps in data:
        if rps[-1] == 'X':
            score += 1
        elif rps[-1] == 'Y':
            score += 2
        elif rps[-1] == 'Z':
            score += 3

        if rps == 'A X':
            score += 3
        elif rps == 'A Y':
            score += 6
        elif rps == 'A Z':
            score += 0
        elif rps == 'B X':
            score += 0
        elif rps == 'B Y':
            score += 3
        elif rps == 'B Z':
            score += 6
        elif rps == 'C X':
            score += 6
        elif rps == 'C Y':
            score += 0
        elif rps == 'C Z':
            score += 3
    return score


def func2(data):
    me_score = 0
    for rps in data:
        if rps[-1] == 'X':
            me_score += 0
            if rps[0] == 'A':
                me_score += 3
            elif rps[0] == 'B':
                me_score += 1
            elif rps[0] == 'C':
                me_score += 2
        elif rps[-1] == 'Y':
            me_score += 3
            if rps[0] == 'A':
                me_score += 1
            elif rps[0] == 'B':
                me_score += 2
            elif rps[0] == 'C':
                me_score += 3
        elif rps[-1] == 'Z':
            me_score += 6
            if rps[0] == 'A':
                me_score += 2
            elif rps[0] == 'B':
                me_score += 3
            elif rps[0] == 'C':
                me_score += 1
    return me_score


def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    #data = [row.split() for row in data]

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
