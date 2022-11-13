letterMap = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'x': 23,
    'y': 24,
    'z': 25
}


def checkStraight3Letters(pw_nbr):
    lastDiff = 0
    for (idx, nbr) in enumerate(pw_nbr[:-1]):
        currentDiff = pw_nbr[idx + 1] - nbr
        if lastDiff == 1 and currentDiff == 1:
            return True
        lastDiff = currentDiff
    return False


def checkNotContainingLetters(pw_nbr):
    unwantedLetters = list(map(lambda x: letterMap.get(x), ['i', 'l', 'o']))
    for unwantedLetter in unwantedLetters:
        if unwantedLetter in pw_nbr:
            return False
    return True


def checkDoubleLetters(pw_nbr):
    idxs = set()
    for (idx, nbr) in enumerate(pw_nbr[:-1]):
        if pw_nbr[idx + 1] - nbr == 0:
            idxs.add(nbr)
    return len(idxs) > 1


def checkpw(pw_nbr):
    if not checkNotContainingLetters(pw_nbr):
        return False
    elif not checkStraight3Letters(pw_nbr):
        return False
    elif not checkDoubleLetters(pw_nbr):
        return False
    else:
        return True


def iterPw(pw_nbr):
    pw_nbr[-1] += 1
    while 26 in pw_nbr:
        idx = pw_nbr.index(26)
        pw_nbr[idx - 1] += 1
        pw_nbr[idx] -= 25
    return pw_nbr


with open("input.txt") as f:
    pw = list(f.read())
    pw_nbr = list(map(lambda x: letterMap.get(x), pw))

    # Part 1
    while not checkpw(pw_nbr):
        pw_nbr = iterPw(pw_nbr)
    pw_back = list(map(lambda x: list(letterMap.keys())[list(letterMap.values()).index(x)], pw_nbr))
    print("answer 1: " + "".join(pw_back))

    # Part 2
    pw_nbr = iterPw(pw_nbr)
    while not checkpw(pw_nbr):
        pw_nbr = iterPw(pw_nbr)
    pw_back = list(map(lambda x: list(letterMap.keys())[list(letterMap.values()).index(x)], pw_nbr))
    print("answer 2: " + "".join(pw_back))
