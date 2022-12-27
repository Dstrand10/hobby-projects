from collections import defaultdict


class Directory:
    def __init__(self, name, parentDirectory):
        self.name = name
        self.parentDirectory = parentDirectory
        self.directorySize = 0

    def addFileSize(self, size):
        self.directorySize += size
        if self.parentDirectory is None:
            return
        else:
            self.parentDirectory.addFileSize(size)


def main():
    lines = [x for x in open("input.txt").read().split('\n')]

    fs = {"/": Directory("/", None)}
    currentDirectory = None
    for line in lines:
        commands = line.split()
        if commands[1] == "cd":
            if commands[2] == "/":
                currentDirectory = fs["/"]
            elif commands[2] == "..":
                currentDirectory = currentDirectory.parentDirectory
            else:
                currentDirectory = fs[currentDirectory.name + commands[2]]
        elif commands[1] == "ls":
            continue
        elif commands[0] == "dir":
            fs[currentDirectory.name + commands[1]] = Directory(currentDirectory.name + commands[1],
                                                                         currentDirectory)
        elif commands[0].isnumeric():
            currentDirectory.addFileSize(int(commands[0]))

    sol1 = sum([val.directorySize for key, val in fs.items() if val.directorySize < 100000])
    print(f"Solution 1: {sol1}")

    sol2 = min([val.directorySize for key, val in fs.items() if val.directorySize > fs['/'].directorySize - (70000000 - 30000000)])
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
