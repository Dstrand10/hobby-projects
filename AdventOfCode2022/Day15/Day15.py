def func1(sensors_beacons):
    y = 2000000
    min_sb_y = min([sb[0][0] - (sb[2] + 1) for sb in sensors_beacons])
    max_sb_y = max([sb[0][0] + (sb[2] + 1) for sb in sensors_beacons])
    sensors_beacons = [sb for sb in sensors_beacons if abs(sb[0][1] - y) <= sb[2]]
    part1 = set()
    for x in range(min_sb_y, max_sb_y):
        for sb in sensors_beacons:
            if (x, y) != sb[1] and (x, y) != sb[0] and abs(x - sb[0][0]) + abs(y - sb[0][1]) <= sb[2]:
                part1.add((x, y))
    return len(part1)


def findPeriferCoords(sb):
    coords = set()
    r = sb[2]
    s_x = sb[0][0]
    s_y = sb[0][1]
    coords.add((s_x, s_y + r + 1))
    coords.add((s_x, s_y - (r + 1)))
    for i in range(r):
        coords.add((s_x - (r - i + 1), s_y + i))
        coords.add((s_x - (r - i + 1), s_y - i))
        coords.add((s_x + (r - i + 1), s_y + i))
        coords.add((s_x + (r - i + 1), s_y - i))
    return coords


def func2(sensors_beacons):
    xy_min = 0
    xy_max = 4000000
    for sb in sensors_beacons:
        pos_coords = findPeriferCoords(sb)
        for x, y in pos_coords:
            if not (xy_min <= x <= xy_max and xy_min <= y <= xy_max):
                continue
            isFree = True
            other_sbs = sensors_beacons.copy()
            other_sbs.remove(sb)
            for other_sb in other_sbs:
                if (x, y) != other_sb[1] and (x, y) != other_sb[0] and abs(x - other_sb[0][0]) + abs(
                        y - other_sb[0][1]) <= other_sb[2]:
                    isFree = False
                    break
            if isFree:
                return x * 4000000 + y


def main():
    # data = [line.strip() for line in open("input.txt").readlines()]
    # data = open("input.txt").read()
    data = open("input.txt").read().split("\n")
    # data = [row.split() for row in data]

    sensors_beacons = []
    for row in data:
        sensor = (int(row.split(":")[0].split("=")[1].split(",")[0]), int(row.split(":")[0].split("=")[2]))
        beacon = (int(row.split(":")[1].split("=")[1].split(",")[0]), int(row.split(":")[1].split("=")[2]))
        manh_dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensors_beacons.append((sensor, beacon, manh_dist))

    # takes 2 min
    sol1 = func1(sensors_beacons)
    print(f"Solution 1: {sol1}")
    sol2 = func2(sensors_beacons)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
