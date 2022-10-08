from collections import defaultdict, deque


def func1(in_data):
    sum = 0
    pairDict = {"(": ")", "{": "}", "[": "]", "<": ">"}
    memory = defaultdict(int)
    for row in in_data:
        deq = deque()
        for char in row:
            memory[char] += 1
            if char in list(pairDict.keys()):
                deq.append(char)
            elif pairDict[deq.pop()] == char:
                continue
            else:
                if char == ")":
                    sum += 3
                elif char == "}":
                    sum += 1197
                elif char == "]":
                    sum += 57
                elif char == ">":
                    sum += 25137

    return sum



def func2(in_data):
    scores = []
    pairDict = {"(": ")", "{": "}", "[": "]", "<": ">"}
    incompleteRows = []
    for row in in_data:
        deq = deque()
        isRowCorrupted = False
        for char in row:
            if char in list(pairDict.keys()):
                deq.append(char)
            elif pairDict[deq.pop()] == char:
                continue
            else:
                isRowCorrupted = True
                break
        if not isRowCorrupted:
            incompleteRows.append(row)

    for row in incompleteRows:
        deq = deque()
        for char in row:
            if char in list(pairDict.keys()):
                deq.append(char)
            elif pairDict[deq[-1]] == char:
                deq.pop()
        row_score = 0
        for id in range(len(deq)):
            row_score = 5 * row_score
            char = pairDict[deq.pop()]
            if char == ")":
                row_score += 1
            elif char == "]":
                row_score += 2
            elif char == "]":
                row_score += 2
            elif char == "}":
                row_score += 3
            elif char == ">":
                row_score += 4
        scores.append(row_score)
    scores.sort()
    return scores[int(len(scores)/2)]


def main():
    in_data = None
    with open("input.txt") as f:
        in_data = f.read().split("\n")

    sol1 = func1(in_data)
    print(f"Solution 1: {sol1}")

    sol2 = func2(in_data)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
