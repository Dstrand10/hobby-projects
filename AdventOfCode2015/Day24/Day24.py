import math


def subset_sum(numbers, target, partial=None, partial_sum=0):
    if partial is None:
        partial = []
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    if len(partial) > 5:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


def daniel_subset_sum(numbers, target, partial=None, partial_sum=0):
    if partial is None:
        partial = []
    if partial_sum == sum(numbers):
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from daniel_subset_sum(remaining, target, partial + [n], partial_sum + n)


with open("input.txt") as f:
    data = [int(line.strip()) for line in f.readlines()]
    groupWeight = int(sum(data) / 3)
    print(groupWeight)
    possibleFrontComps = list(subset_sum(data, groupWeight))
    possibleFrontComps.sort(key=lambda x: math.prod(x))
    min_qe = math.inf
    for posFrontComp in possibleFrontComps:
        otherComp = list(daniel_subset_sum([x for x in data if x not in posFrontComp], groupWeight))
        tmp_qe = math.prod(posFrontComp)
        if otherComp and tmp_qe < min_qe:
            min_qe = tmp_qe
            break
    print(min_qe) #11846773891

    groupWeight = int(sum(data) / 4)
    print(groupWeight)
    possibleFrontComps = list(subset_sum(data, groupWeight))
    possibleFrontComps.sort(key=lambda x: math.prod(x))
    min_qe = math.inf
    breakAll = False
    for posFrontComp in possibleFrontComps:
        otherComp = list(daniel_subset_sum([x for x in data if x not in posFrontComp], groupWeight))
        possibleFrontComps2 = list(subset_sum(posFrontComp, groupWeight))
        possibleFrontComps2.sort(key=lambda x: math.prod(x))
        for posFrontComp2 in possibleFrontComps2:
            otherComp2 = list(daniel_subset_sum([x for x in data if x not in posFrontComp2], groupWeight))
            tmp_qe = math.prod(posFrontComp)
            if otherComp and tmp_qe < min_qe:
                min_qe = tmp_qe
                breakAll = True
            if breakAll:
                break
        if breakAll:
            break
    print(min_qe)  # 11846773891