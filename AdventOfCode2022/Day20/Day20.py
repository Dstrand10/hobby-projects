def solve(data, iterations, encryption):
    size = len(data)
    numbers = [(idx, nbr * encryption % (size - 1), nbr * encryption) for idx, nbr in enumerate(data)]
    for i in range(iterations):
        print("Iteration:", i + 1)
        for j in range(size):
            start_idx, move_steps, nbr = [x for x in numbers if x[0] == j][0]
            curr_idx = numbers.index((start_idx, move_steps, nbr))
            new_idx = (curr_idx + move_steps) % (size - 1)
            numbers.remove((start_idx, move_steps, nbr))
            if new_idx == 0:
                numbers.append((start_idx, move_steps, nbr))
            else:
                numbers.insert(new_idx, (start_idx, move_steps, nbr))
    ans = 0
    zero_idx = numbers.index([x for x in numbers if x[2] == 0][0])
    for k in [1000, 2000, 3000]:
        ans += numbers[(zero_idx + k) % size][2]
    return ans


def main():
    data = list(map(int, open("input.txt").read().split("\n")))

    sol1 = solve(data, 1, 1)
    print(f"Solution 1: {sol1}")
    sol2 = solve(data, 10, 811589153)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
