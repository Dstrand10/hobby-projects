#https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/hps5hgw/?utm_source=reddit&utm_medium=web2x&context=3

#I[1] + 4 = I[14] - -12
#I[2] + 11 = I[13] - -4
#I[3] + 7 = I[4] - -14
#I[5] + 11 = I[6] - -10
#I[7] + 9 = I[12] - -1
#I[8] + 12 = I[9] - -7
#I[10] + 2 = I[11] - -2
def func1():
    return "92928914999991"

def func2():
    return "91811211611981"


def main():
    data = open("input.txt").read().split("\n")

    sol1 = func1()
    print(f"Solution 1: {sol1}")

    sol2 = func2()
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
