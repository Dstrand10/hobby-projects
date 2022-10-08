#

def find_valid_passwords_first_method(input_data):
    count_valid_pws = 0
    for pw_row in input_data:
        criteria, pw = pw_row.split(": ")
        lower_bound, _ = criteria.split("-")
        ph_1, letter = criteria.split(" ")
        _, upper_bound = ph_1.split("-")
        if int(lower_bound) <= pw.count(letter) <= int(upper_bound):
            count_valid_pws += 1
    return count_valid_pws


def find_valid_passwords_second_method(input_data):
    count_valid_pws = 0
    for pw_row in input_data:
        criteria, pw = pw_row.split(": ")
        lower_index, _ = criteria.split("-")
        ph_1, letter = criteria.split(" ")
        _, upper_index = ph_1.split("-")
        if (pw[int(lower_index) - 1] == letter or pw[int(upper_index) - 1] == letter) and pw[int(lower_index) - 1] != pw[
            int(upper_index) - 1]:
            count_valid_pws += 1
    return count_valid_pws


def main():
    with open('input.txt') as f:
        input_data = list(map(str, f))
        nbr_of_valid_pws = find_valid_passwords_first_method(input_data)
        print(f"Solution 1: {nbr_of_valid_pws}")

        nbr_of_valid_pws_2 = find_valid_passwords_second_method(input_data)
        print(f"Solution 2: {nbr_of_valid_pws_2}")


if __name__ == "__main__":
    main()
