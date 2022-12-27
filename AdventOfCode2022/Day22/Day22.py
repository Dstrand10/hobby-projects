from dataclasses import dataclass

# EdgeConnection: (edge, direction=None, reverse=None)
@dataclass
class EdgeConnection:
    edge: tuple[tuple[int, int]]
    newDir: str = None
    reverse: bool = None

# EdgeConnection: (edge, direction=None, reverse=None)
@dataclass
class Dirs:
    dir: tuple
    left: str
    right: str

DIRS = {
    "^": Dirs((-1, 0), "<", ">"),
    ">": Dirs((0, 1), "^", "v"),
    "v": Dirs((1, 0), ">", "<"),
    "<": Dirs((0, -1), "v", "^")
}




def get_edge_connections():
    oneA = tuple([(-1, i) for i in range(100, 150)])
    oneB = tuple([(i, 150) for i in range(0, 50)])
    oneC = tuple([(50, i) for i in range(100, 150)])
    twoA = tuple([(-1, i) for i in range(50, 100)])
    twoD = tuple([(i, 49) for i in range(0, 50)])
    threeB = tuple([(i, 100) for i in range(50, 100)])
    threeD = tuple([(i, 49) for i in range(50, 100)])
    fourB = tuple([(i, 100) for i in range(100, 150)])
    fourC = tuple([(150, i) for i in range(50, 100)])
    fiveA = tuple([(99, i) for i in range(0, 50)])
    fiveD = tuple([(i, -1) for i in range(100, 150)])
    sixB = tuple([(i, 50) for i in range(150, 200)])
    sixC = tuple([(200, i) for i in range(0, 50)])
    sixD = tuple([(i, -1) for i in range(150, 200)])

    edge_conn_part1 = {
        oneA: EdgeConnection(oneC),
        oneB: EdgeConnection(twoD),
        oneC: EdgeConnection(oneA),
        twoA: EdgeConnection(fourC),
        twoD: EdgeConnection(oneB),
        threeB: EdgeConnection(threeD),
        threeD: EdgeConnection(threeB),
        fourB: EdgeConnection(fiveD),
        fourC: EdgeConnection(twoA),
        fiveA: EdgeConnection(sixC),
        fiveD: EdgeConnection(fourB),
        sixB: EdgeConnection(sixD),
        sixC: EdgeConnection(fiveA),
        sixD: EdgeConnection(sixB)
    }

    edge_conn_part2 = {
        oneA: EdgeConnection(sixC, "^", False),
        oneB: EdgeConnection(fourB, "<", True),
        oneC: EdgeConnection(threeB, "<", False),
        twoA: EdgeConnection(sixD, ">", False),
        twoD: EdgeConnection(fiveD, ">", True),
        threeB: EdgeConnection(oneC, "^", False),
        threeD: EdgeConnection(fiveA, "v", False),
        fourB: EdgeConnection(oneB, "<", True),
        fourC: EdgeConnection(sixB, "<", False),
        fiveA: EdgeConnection(threeD, ">", False),
        fiveD: EdgeConnection(twoD, ">", True),
        sixB: EdgeConnection(fourC, "^", False),
        sixC: EdgeConnection(oneA, "v", False),
        sixD: EdgeConnection(twoA, "v", False)
    }
    return edge_conn_part1, edge_conn_part2


def find_pos_after_edge(next_pos, dir, edge_connections):
    for edge, edge_conn in edge_connections.items():
        if next_pos in edge:
            pos_id = edge.index(next_pos)
            new_dir = dir if edge_conn.newDir is None else edge_conn.newDir
            connected_edge_pos = edge_conn.edge[49 - pos_id] if edge_conn.reverse else edge_conn.edge[pos_id]
            return (connected_edge_pos[0] + DIRS[new_dir].dir[0], connected_edge_pos[1] + DIRS[new_dir].dir[1]), new_dir


def walk_in_cave(curr_pos, dir, steps, tiles, walls, edge_connections):
    step_dir = DIRS[dir].dir
    for step in range(steps):
        next_pos = (curr_pos[0] + step_dir[0], curr_pos[1] + step_dir[1])
        if next_pos in walls:
            return curr_pos, dir
        elif next_pos not in tiles:
            next_pos, new_dir = find_pos_after_edge(next_pos, dir, edge_connections)
            if next_pos in walls:
                return curr_pos, dir
            else:
                curr_pos, dir = next_pos, new_dir
            step_dir = DIRS[dir].dir
        else:
            curr_pos = next_pos
    return curr_pos, dir


def solve(start_pos, instructions, tiles, walls, edge_conn):
    # iterating over instructions
    curr_pos = start_pos
    steps = ''
    dir = ">"
    for char in instructions:
        if char.isdigit():
            steps += char
        elif char == "R" or char == "L":
            curr_pos, dir = walk_in_cave(curr_pos, dir, int(steps), tiles, walls, edge_conn)
            dir = DIRS[dir].left if char == "L" else DIRS[dir].right
            steps = ''
        else:
            print("ERROR")

    curr_pos, dir = walk_in_cave(curr_pos, dir, int(steps), tiles, walls, edge_conn)
    return (curr_pos[0] + 1) * 1000 + (curr_pos[1] + 1) * 4 + [">", "v", "<", "^"].index(dir)


def main():
    data = open("input.txt").read().split("\n\n")

    tiles = set()
    walls = set()
    start_pos = None
    for rowid, row in enumerate(data[0].split("\n")):
        for colid, cell in enumerate(row):
            if cell == ".":
                tiles.add((rowid, colid))
                if start_pos is None:
                    start_pos = (rowid, colid)
            if cell == "#":
                walls.add((rowid, colid))

    edge_conn_part1, edge_conn_part2 = get_edge_connections()
    sol1 = solve(start_pos, data[1], tiles, walls, edge_conn_part1)
    print("Solution 1:", sol1)
    sol2 = solve(start_pos, data[1], tiles, walls, edge_conn_part2)
    print("Solution 2:", sol2)


if __name__ == "__main__":
    main()
