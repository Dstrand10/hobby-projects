from copy import deepcopy
from functools import cmp_to_key


def checkLists(item1, item2):
    if isinstance(item1, int) and isinstance(item2, int):
        if item1 < item2:
            return -1
        elif item1 > item2:
            return 1
        else:
            return 0
    elif isinstance(item1, int) and isinstance(item2, list):
        check = checkLists([item1], item2)
    elif isinstance(item1, list) and isinstance(item2, int):
        check = checkLists(item1, [item2])
    else:
        while item1 and item2:
            entity1 = item1.pop(0)
            entity2 = item2.pop(0)
            check = checkLists(entity1, entity2)
            if check != 0:
                return check
        if not item1 and item2:
            return -1
        elif item1 and not item2:
            return 1
        else:
            return 0
    return check


def func1(data):
    listsWorkingIndex = []
    for idx, row in enumerate(data):
        row_split = row.split()
        list1 = list(eval(row_split[0]))
        list2 = list(eval(row_split[1]))
        if checkLists(deepcopy(list1), deepcopy(list2.copy())) == -1:
            listsWorkingIndex.append(idx + 1)
    return sum(listsWorkingIndex)


def func2(data):
    all_lists = []
    for idx, row in enumerate(data):
        list1, list2 = row.split()
        all_lists.append(list(eval(list1)))
        all_lists.append(list(eval(list2)))
    all_lists.append([[2]])
    all_lists.append([[6]])
    sorted_all_list = sorted(all_lists, key=cmp_to_key(lambda x, y: checkLists(deepcopy(x), deepcopy(y))))
    return (sorted_all_list.index([[2]]) + 1) * (sorted_all_list.index([[6]]) + 1)


def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n\n")
    # data = [row.split() for row in data]
    sol1 = func1(data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
