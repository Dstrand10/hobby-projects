import numpy as np


def calc_operator(number_str, operator):
    if operator == "+":
        return int(number_str[0]) + int(number_str[1])
    elif operator == "*":
        return int(number_str[0]) * int(number_str[1])
    else:
        print("Something went wrong in evaluation.")


def calc_parenthesis(row, function):
    new_row = row
    while "(" in new_row:
        left_par_idx = [idx for idx, x in enumerate(new_row) if x == "("]
        right_par_idx = [idx for idx, x in enumerate(new_row) if x == ")"]
        max_dist = np.Inf
        for left_par in left_par_idx:
            for right_par in right_par_idx:
                dist = right_par - left_par
                if 0 < dist < max_dist:
                    left_par_couple = left_par
                    right_par_couple = right_par
                    max_dist = dist

        expression = new_row[left_par_couple + 1: right_par_couple]
        amount = function(expression)
        new_row = new_row[:left_par_couple] + str(amount) + new_row[right_par_couple + 1:]

    return function(new_row)


def evaluate_expression_sol1(expression: str):
    idx_first_nbr = 0
    number_str = ['', '']
    operator = ''

    new_expression = expression
    count = 0
    while "+" in new_expression or "*" in new_expression:

        if count == len(new_expression) or \
                (idx_first_nbr > 0 and not new_expression[count].isnumeric() and (
                        number_str[0] != '' and number_str[1] != '')):
            new_expression = new_expression[:count - nbr_idx_start - 1] + str(
                calc_operator(number_str, operator)) + new_expression[count + 1:]
            idx_first_nbr = 0
            number_str = ['', '']
            operator = ''
            count = 0

        if new_expression[count] == " ":
            count += 1
            continue

        if new_expression[count].isnumeric():
            nbr_idx_start = count
            number_str[idx_first_nbr] = number_str[idx_first_nbr] + new_expression[count]
            count += 1
            continue

        if new_expression[count] == "+" or new_expression[count] == "*":
            operator = new_expression[count]
            idx_first_nbr += 1
            count += 1

    total_amount = int(new_expression)

    return total_amount


def evaluate_expression_sol2(expression: str):
    new_expression = expression
    while "+" in new_expression:
        plus_operator_idx = new_expression.find("+")
        right_nbr = ''
        right_nbr_end_idx = -1
        left_nbr = ''
        left_nbr_end_idx = -1
        count = plus_operator_idx + 1
        while True:
            if count >= len(new_expression):
                right_nbr_end_idx = count - 1
                break
            elif new_expression[count] == " ":
                count += 1
                continue
            elif new_expression[count].isnumeric():
                right_nbr = right_nbr + new_expression[count]
                count += 1
            else:
                right_nbr_end_idx = count - 1
                break
        count = plus_operator_idx - 1
        while True:
            if count < 0:
                left_nbr_end_idx = count + 1
                break
            elif new_expression[count] == " ":
                count -= 1
                continue
            elif new_expression[count].isnumeric():
                left_nbr = new_expression[count] + left_nbr
                count -= 1
            else:
                left_nbr_end_idx = count + 1
                break
        amount = calc_operator([left_nbr, right_nbr], "+")
        new_expression = new_expression[:left_nbr_end_idx] + " " + str(amount) + " " + new_expression[right_nbr_end_idx + 1:]

    return evaluate_expression_sol1(new_expression)


def solution_1(input_data):
    total_amount = 0
    for row in input_data:
        amount = calc_parenthesis(row, evaluate_expression_sol1)
        total_amount += amount
    return total_amount


def solution_2(input_data):
    total_amount = 0
    for row in input_data:
        amount = calc_parenthesis(row, evaluate_expression_sol2)
        total_amount += amount
    return total_amount


def main():
    input_data = open('input.txt', "r").read().split("\n")

    sol1 = solution_1(input_data)
    print(f"Solution 1: {sol1}")

    sol2 = solution_2(input_data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
