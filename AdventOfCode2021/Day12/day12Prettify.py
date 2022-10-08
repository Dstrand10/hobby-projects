from collections import defaultdict, deque

in_data = open("input.txt").read().split("\n")
cave_connections = defaultdict(list)
for row in in_data:
    a, b = row.split("-")
    cave_connections[a].append(b)
    cave_connections[b].append(a)

def func(p1):
    only_visit_once = set(["start"])
    start = ("start", only_visit_once, False)
    Q = deque([start])
    ans = 0
    while Q:
        current_cave, only_visit_once, twice = Q.popleft()
        if current_cave == "end":
            ans += 1
            continue
        for next_cave in cave_connections[current_cave]:
            if next_cave not in only_visit_once:
                new_only_visit_once = set(only_visit_once)
                if next_cave.lower() == next_cave:
                    new_only_visit_once.add(next_cave)
                Q.append((next_cave, new_only_visit_once, twice))
            elif next_cave in only_visit_once and not p1 and not twice and next_cave not in ["start", "end"]:
                Q.append((next_cave, only_visit_once, True))
    return ans

print("Solution 1: " + str(func(True)))
print("Solution 2: " + str(func(False)))
