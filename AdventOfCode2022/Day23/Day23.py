from collections import defaultdict


def show(elves):
    print()
    row_coords = [k[0] for k, _ in elves.items()]
    col_coords = [k[1] for k, _ in elves.items()]
    for i in range(min(row_coords), max(row_coords) + 1):
        tmp_list = []
        for j in range(min(col_coords), max(col_coords) + 1):
            if (i, j) in elves.keys():
                tmp_list.append("#")
            else:
                tmp_list.append(".")
        print(''.join(tmp_list))
    print()


def func1(elves):
    show(elves)

    cardinals = [((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1)), ((-1, -1), (0, -1), (1, -1)),
                 ((-1, 1), (0, 1), (1, 1))]
    for i in range(10):
        proposed_new_pos = dict()
        new_pos_elves = dict()
        for elf, _ in elves.items():
            adjacent_elf = False
            for adjacent in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if (elf[0] + adjacent[0], elf[1] + adjacent[1]) in elves.keys():
                    adjacent_elf = True
            if not adjacent_elf:
                proposed_new_pos[elf] = elf
                continue

            for cardinal in cardinals:
                poss_next_move_elf = True
                for dir in cardinal:
                    if (elf[0] + dir[0], elf[1] + dir[1]) in elves.keys():
                        poss_next_move_elf = False
                        break

                if poss_next_move_elf:
                    proposed_new_pos[elf] = (elf[0] + cardinal[1][0], elf[1] + cardinal[1][1])
                    break
            if poss_next_move_elf:
                continue
            else:
                proposed_new_pos[elf] = elf
                
        for elf, new_pos in proposed_new_pos.items():
            if list(proposed_new_pos.values()).count(new_pos) == 1:
                new_pos_elves[new_pos] = elf
            else:
                new_pos_elves[elf] = elf

        elves = new_pos_elves

        show(elves)  #Prints elves
        tmp_cardinal = cardinals.pop(0)
        cardinals.append(tmp_cardinal)

    row_coords = [k[0] for k, _ in elves.items()]
    col_coords = [k[1] for k, _ in elves.items()]

    return (max(row_coords) - min(row_coords) + 1) * (max(col_coords) - min(col_coords) + 1) - len(elves)


def func2(elves):
    cardinals = [((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1)), ((-1, -1), (0, -1), (1, -1)),
                 ((-1, 1), (0, 1), (1, 1))]
    cnt = 0
    while True:
        cnt += 1
        proposed_new_pos = dict()
        new_pos_elves = dict()
        for elf, _ in elves.items():
            adjacent_elf = False
            for adjacent in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if (elf[0] + adjacent[0], elf[1] + adjacent[1]) in elves.keys():
                    adjacent_elf = True
            if not adjacent_elf:
                proposed_new_pos[elf] = elf
                continue

            for cardinal in cardinals:
                poss_next_move_elf = True
                for dir in cardinal:
                    if (elf[0] + dir[0], elf[1] + dir[1]) in elves.keys():
                        poss_next_move_elf = False
                        break

                if poss_next_move_elf:
                    proposed_new_pos[elf] = (elf[0] + cardinal[1][0], elf[1] + cardinal[1][1])
                    break
            if poss_next_move_elf:
                continue
            else:
                proposed_new_pos[elf] = elf

        for elf, new_pos in proposed_new_pos.items():
            if list(proposed_new_pos.values()).count(new_pos) == 1:
                new_pos_elves[new_pos] = elf
            else:
                new_pos_elves[elf] = elf

        if list(new_pos_elves.keys()) == list(elves.keys()):
            break
        else:
            elves = new_pos_elves
        tmp_cardinal = cardinals.pop(0)
        cardinals.append(tmp_cardinal)
    return cnt


def parse_data(data):
    elves = defaultdict(str)
    for rowid, row in enumerate(data):
        for colid, point in enumerate(row):
            if point == "#":
                elves[(rowid, colid)] = (None, None)
    return elves


def main():
    data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    elves = parse_data(data)
    print(elves)
    # data = [row.split() for row in data]

    sol1 = func1(elves)
    print(f"Solution 1: {sol1}")

    sol2 = func2(elves)
    print(f"Solution 1: {sol2}")


if __name__ == "__main__":
    main()
