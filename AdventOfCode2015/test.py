a = [1, 2, 3, 4, 5, 6, 7, 8]


def even(ints):
    for int in ints:
        if int % 2 == 0:
            yield int


print(list(even(a)))
