from collections import defaultdict


def func(in_data, nbr_of_iterations):
    pairs_exists = defaultdict(int)
    elem = in_data[0]
    for i in range(len(elem) - 1):
        pairs_exists[elem[i] + elem[i + 1]] += 1

    for i in range(nbr_of_iterations):
        rules = in_data[1].split("\n")
        tmp_pairs = defaultdict(int)
        for rule in rules:
            first_rule, second_rule = rule.split(" -> ")
            if first_rule in pairs_exists.keys():
                tmp_pairs[first_rule[0] + second_rule] += pairs_exists[first_rule]
                tmp_pairs[second_rule + first_rule[1]] += pairs_exists[first_rule]
        pairs_exists = tmp_pairs

    chars = defaultdict(int)
    for key, val in pairs_exists.items():
        chars[key[0]] += val
    chars[elem[-1]] += 1

    return max(chars.values()) - min(chars.values())


def main():
    in_data = open("input.txt").read().split("\n\n")

    sol1 = func(in_data, 10)
    print(f"Solution 1: {sol1}")

    sol2 = func(in_data, 40)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
