def main():
    # data = [int(line.strip()) for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n\n")
    data = list(map(lambda x: sum(list(map(int, x.split("\n")))), data))
    print(f"Solution 1: {max(data)}")
    data.sort()
    print(f"Solution 2: {sum(data[-3:])}")


if __name__ == "__main__":
    main()
