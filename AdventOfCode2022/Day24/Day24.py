from collections import deque


def simulate_blizzards(start_pos, end_pos, l, w, blizzards):
    orig_blizzards = blizzards.copy()
    all_blizzards = dict()
    i = 0
    all_blizzards[i] = (blizzards.copy(), frozenset([(x, y) for x, y, _ in blizzards]))
    # show_blizzard(start_pos, end_pos, (-1, 0), l, w, blizzards)
    while True:
        i += 1
        tmp_blizzards = list()
        for row, col, dir in blizzards:
            if dir == ">":
                tmp_blizzards.append((row, (col + 1) % w, dir))
            elif dir == "v":
                tmp_blizzards.append(((row + 1) % l, col, dir))
            elif dir == "<":
                tmp_blizzards.append((row, (col - 1) % w, dir))
            else:
                tmp_blizzards.append(((row - 1) % l, col, dir))

        # show_blizzard(start_pos, end_pos, (-1, 0), l, w, tmp_blizzards)
        if tmp_blizzards == orig_blizzards:
            break

        all_blizzards[i] = (tmp_blizzards.copy(), frozenset([(x, y) for x, y, _ in tmp_blizzards]))
        blizzards = tmp_blizzards

    return all_blizzards


def show_blizzard(start_pos, end_pos, curr_pos, l, w, blizzards):
    print()
    print_list = []
    for i in range(l):
        row = '#'
        for j in range(w):
            blizzes = [(row, col, dir) for row, col, dir in blizzards if i == row and j == col]
            if (i, j) == curr_pos:
                row += "E"
            elif len(blizzes) == 1:
                row += str(blizzes[0][2])
            elif len(blizzes) > 1:
                row += str(len(blizzes))
            else:
                row += "."
        row += '#'
        print_list.append(row)
    print("#" + ("E" if curr_pos == start_pos else ".") + "#" * w)
    for row in print_list:
        print(row)
    print("#" * w + ("E" if curr_pos == end_pos else ".") + "#")
    print()


def func1(start_pos, end_pos, blizzards):
    l = end_pos[0] - start_pos[0] - 1
    w = end_pos[1] - start_pos[1] + 1

    all_blizzards = simulate_blizzards(start_pos, end_pos, l, w, blizzards)
    DIR = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
    Q = deque([(start_pos[0], start_pos[1], 0, False, False)])
    SEEN = set()
    sol1 = None
    while Q:
        row, col, time, visited_goal, visited_start_again = Q.popleft()
        next_blizzard = all_blizzards[(time + 1) % len(all_blizzards)]

        if ((row, col), time, visited_goal, visited_start_again) in SEEN:
            continue
        SEEN.add(((row, col), time, visited_goal, visited_start_again))

        for dir in DIR:
            new_row = row + dir[0]
            new_col = col + dir[1]

            if (new_row, new_col) == end_pos and sol1 is None:
                sol1 = time + 1
                visited_goal = True
            if (new_row, new_col) == start_pos and visited_goal:
                visited_start_again = True
            if (new_row, new_col) == end_pos and visited_goal and visited_start_again:
                return sol1, time + 1

            if (0 <= new_row < l and 0 <= new_col < w) or (new_row, new_col) == start_pos:
                if (new_row, new_col) not in next_blizzard[1]:
                    # print("current pos: ", (new_row, new_col), "Minute: ", time + 1)
                    # show_blizzard(start_pos, end_pos, (new_row, new_col), l, w, next_blizzard[0])
                    Q.append((new_row, new_col, time + 1, visited_goal, visited_start_again))


def parse_data(data):
    start_pos = (-1, 0)
    end_pos = (len(data) - 2, len(data[0]) - 3)
    blizzards = list()
    for rowid, row in enumerate(data):
        for colid, dir in enumerate(row):
            if dir in "<^>v":
                blizzards.append((rowid - 1, colid - 1, dir))
    return start_pos, end_pos, blizzards


def main():
    data = open("input.txt").read().split("\n")
    start_pos, end_pos, blizzards = parse_data(data)

    sol1, sol2 = func1(start_pos, end_pos, blizzards)
    print(f"Solution 1:", sol1)
    print(f"Solution 2:", sol2)


if __name__ == "__main__":
    main()
