input = open("input.txt").read().split("\n")

opener = {"(": ")", "{": "}", "[": "]", "<": ">"}
closer = {"}": "{", "]": "[", ")": "(", ">": "<"}
tot_sum_corrupted = 0
tot_sum_insufficient = []
for row in input:
    chars = []
    for char in row:
        if char in opener:
            chars.append(char)
            continue
        if char in closer and chars.pop() != closer[char]:
            tot_sum_corrupted += {")": 3, "]": 57, "}": 1197, ">": 25137}[char]
            break
    else:
        sum = 0
        while chars:
            char = chars.pop()
            sum *= 5
            sum += {")": 1, "]": 2, "}": 3, ">": 4}[opener[char]]
        tot_sum_insufficient.append(sum)

print("Solution 1: " + str(tot_sum_corrupted))
tot_sum_insufficient.sort()
print("Solution 2: " + str(tot_sum_insufficient[int(len(tot_sum_insufficient)/2)]))