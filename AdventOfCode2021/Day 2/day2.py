class Submarine:

    def __init__(self):
        self.depth = 0
        self.horizontal_pos = 0
        self.aim = 0

    def move_forward(self, forward):
        self.horizontal_pos += forward
        return self

    def move_depth(self, move_depth):
        self.depth += move_depth
        return self

    def change_aim(self, change_aim):
        self.aim += change_aim
        return self

    def move_forward_with_aim(self, forward):
        self.horizontal_pos += forward
        self.depth += self.aim * forward
        return self


def func1(in_data):
    submarine = Submarine()
    for row in in_data:
        cmd, nbr = row.split(" ")
        nbr = int(nbr)
        if cmd == "forward":
            submarine.move_forward(nbr)
        elif cmd == "down":
            submarine.move_depth(nbr)
        elif cmd == "up":
            submarine.move_depth(-nbr)
    return submarine.depth * submarine.horizontal_pos


def func2(in_data):
    submarine = Submarine()
    for row in in_data:
        cmd, nbr = row.split(" ")
        nbr = int(nbr)
        if cmd == "forward":
            submarine.move_forward_with_aim(nbr)
        elif cmd == "down":
            submarine.change_aim(nbr)
        elif cmd == "up":
            submarine.change_aim(-nbr)
    return submarine.depth * submarine.horizontal_pos


def main():
    with open('input.txt') as f:
        in_data = list(f)

        sol1 = func1(in_data)
        print(f"Solution 1: {sol1}")

        sol2 = func2(in_data)
        print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
