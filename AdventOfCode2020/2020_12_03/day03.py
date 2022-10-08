def sol_1(input_data, step_right):
    width = len(input_data[1]) - 1  # Minus one for blank row
    count_trees = 0
    right_coordinate = 3
    for index, line in enumerate(input_data[1:]):  # Don't need the first row
        if line[right_coordinate] == "#":
            # print("Row: " + str(index) + ": " + "right_coord: " + str(right_coordinate))
            count_trees += 1
        right_coordinate += step_right
        right_coordinate = right_coordinate % width  # Modulus the width of the data
    return count_trees


def sol_2(input_data, step_right, step_down):
    width = len(input_data[1]) - 1  # Minus one for blank row
    length = len(input_data)
    count_trees = 0
    right_coord = step_right  # This means we're not checking the starting position (0,0) since it is always fine
    down_coord = step_down
    while down_coord < length:
        if input_data[down_coord][right_coord] == "#":
            count_trees += 1
        right_coord += step_right
        right_coord = right_coord % width  # Modulus the width of the data
        down_coord += step_down

    return count_trees


def main():
    with open('input.txt') as f:
        input_data = list(map(str, f))
        step_right = 3
        sol1 = sol_1(input_data, step_right)
        print(f"Solution 1: {sol1}")
        sol2 = 1
        for step_right, step_down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
            tmp_sol2 = sol_2(input_data, step_right, step_down)
            sol2 *= tmp_sol2
        print("Solution 2: " + str(sol2))


if __name__ == "__main__":
    main()
