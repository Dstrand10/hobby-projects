import numpy as np

with open("input.txt") as f:
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    data = [(x.split(" ")[0], x.split(" ")[2], x.split(" ")[-1]) for x in lines]
    destinations = list(set([x[0] for x in data] + [x[1] for x in data]))
    g = np.ones((len(destinations), len(destinations))) * np.inf
    print(destinations)
    print(g)
    for d in data:
        x = destinations.index(d[0])
        y = destinations.index(d[1])
        g[x][y] = d[2]
    print(g)

    ans = np.ones((len(destinations), len(destinations))) * np.inf
    
