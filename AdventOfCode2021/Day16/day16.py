sumVersions = 0

def lookForward(data, n):
    ret = data[0][:n]
    data[0] = data[0][n:]
    return ret

def parse(data):
    version = int(lookForward(data, 3), 2)
    global sumVersions
    sumVersions += version
    tid = int(lookForward(data, 3), 2)
    if tid == 4:
        t = []
        while True:
            cnt, *v = lookForward(data, 5)
            t += v
            if cnt == '0':
                break
        return int("".join(t), 2)

    ltid = lookForward(data, 1)[0]
    spv = []
    if ltid == "0":
        subpacklength = int(lookForward(data, 15), 2)
        subpackets = [lookForward(data, subpacklength)]
        while subpackets[0]:
            spv.append(parse(subpackets))
    else:
        spv = [parse(data) for _ in range(int(lookForward(data, 11), 2))]

    if tid == 0:
        return sum(spv)
    elif tid == 1:
        p = 1
        for x in spv:
            p *= x
        return p
    elif tid == 2:
        return min(spv)
    elif tid == 3:
        return max(spv)
    elif tid == 5:
        return int(spv[0] > spv[1])
    elif tid == 6:
        return int(spv[0] < spv[1])
    elif tid == 7:
        return int(spv[0] == spv[1])


def main():
    in_data = open("input.txt").read()
    data = bin(int(in_data, 16))[2:]
    while len(data) < 4 * len(in_data):
        data = "0" + data

    res = parse([data])
    print(f"Solution 1: {sumVersions}")
    print(f"Solution 2: {res}")


if __name__ == "__main__":
    main()
