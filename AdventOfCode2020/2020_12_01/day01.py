# Recursive solution for finding two (part 1) and three (part 2) numbers in the list which adds up to 2020.

def recursive_solution_inf_deep(in_data, final_sum, nbrs_to_add):
    tmp_answer = None
    for index, i in enumerate(in_data):
        if nbrs_to_add > 2:
            tmp_nbr = recursive_solution_inf_deep(in_data[index + 1:], final_sum - i, nbrs_to_add - 1)
            if tmp_nbr is None:
                continue
            else:
                tmp_answer = i * tmp_nbr
        elif nbrs_to_add == 2:
            if final_sum - i in in_data[index + 1:]:
                return i * (final_sum - i)
    return tmp_answer


def main():
    with open('input.txt') as f:
        in_data = list(map(int, f))
        final_sum = 2020
        nbrs_to_add = 2
        print(f"Solution 1: {recursive_solution_inf_deep(in_data, final_sum, nbrs_to_add)}")
        nbrs_to_add = 3
        print(f"Solution 2: {recursive_solution_inf_deep(in_data, final_sum, nbrs_to_add)}")


if __name__ == "__main__":
    main()
