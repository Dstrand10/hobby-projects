import itertools


def func1(data):
    pos_p1 = int(data[0].split("position: ")[1])
    pos_p2 = int(data[1].split("position: ")[1])
    score_p1 = 0
    score_p2 = 0

    roll_count = 1
    while score_p1 < 1000 and score_p2 < 1000:
        rolling = roll_count + roll_count + 1 + roll_count + 2
        if roll_count % 2 == 1:
            pos_p1 += rolling
            pos_p1 = pos_p1 % 10 if pos_p1 % 10 != 0 else 10
            score_p1 += pos_p1
        else:
            pos_p2 += rolling
            pos_p2 = pos_p2 % 10 if pos_p2 % 10 != 0 else 10
            score_p2 += pos_p2
        roll_count += 3
    return (roll_count - 1) * score_p1 if score_p1 < 1000 else (roll_count - 1) * score_p2


roll_sums = list(map(sum, itertools.product([1, 2, 3], [1, 2, 3], [1, 2, 3])))
memory = {}

def moveStepAndCheckWin(p1, p2, s1, s2):
    if (p1, p2, s1, s2) in memory.keys():
        return memory[(p1, p2, s1, s2)]
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    ans = (0, 0)
    for roll in roll_sums:
        p1_new = (p1 + roll) % 10
        s1_new = s1 + p1_new if p1_new != 0 else s1 + 10
        x1, y1 = moveStepAndCheckWin(p2, p1_new, s2, s1_new)
        ans = (ans[0] + y1, ans[1] + x1)
    memory[(p1, p2, s1, s2)] = ans
    return ans


def main():
    data = open("input.txt").read().split("\n")

    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = max(moveStepAndCheckWin(int(data[0].split("position: ")[1]), int(data[1].split("position: ")[1]), 0, 0))
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
