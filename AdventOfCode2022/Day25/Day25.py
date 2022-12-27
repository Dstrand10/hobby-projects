def to_decimal(data):
    ans = 0
    for row in data:
        i = 0
        while row:
            char = row[-1]
            row = row[:-1]
            if char == "=":
                ans += -2 * 5 ** i
            elif char == "-":
                ans += -1 * 5 ** i
            elif char == "1":
                ans += 1 * 5 ** i
            elif char == "2":
                ans += 2 * 5 ** i
            i += 1
    return ans


def main():
    data = open("input.txt").read().split("\n")
    print("Sum all SNAFU to decimal: ", to_decimal(data))

    # Solving by adding in SNAFU
    ans = ""
    carry_over = 0
    for i in range(1, max([len(row) for row in data]) + 1):
        sum_pos_i = carry_over
        for row in data:
            if i <= len(row):
                if row[-i] == "=":
                    sum_pos_i -= 2
                elif row[-i] == "-":
                    sum_pos_i -= 1
                else:
                    sum_pos_i += int(row[-i])
        carry_over = 0
        while sum_pos_i >= 3:
            carry_over += 1
            sum_pos_i -= 5
        while sum_pos_i <= -3:
            carry_over -= 1
            sum_pos_i += 5
        if sum_pos_i == -2:
            ans += "="
        elif sum_pos_i == -1:
            ans += "-"
        else:
            ans += str(sum_pos_i)
    sol1 = ''.join(list(reversed(ans)))

    print(f"Solution 1: {sol1}")


if __name__ == "__main__":
    main()
