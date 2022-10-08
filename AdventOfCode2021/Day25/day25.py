def showMap(R, C, face_right, face_down):
    print()
    map = ["."*C]*R
    for sea_cucumber in face_right:
        rowid = sea_cucumber[0]
        colid = sea_cucumber[1]
        map[rowid] = map[rowid][:colid] + ">" + map[rowid][colid + 1:]
    for sea_cucumber in face_down:
        rowid = sea_cucumber[0]
        colid = sea_cucumber[1]
        map[rowid] = map[rowid][:colid] + "v" + map[rowid][colid + 1:]
    for row in map:
        print(''.join(row))



def func(data):
    R = len(data)
    C = len(data[0])
    face_right = {}
    face_down = {}
    for rowid in range(len(data)):
        for colid in range(len(data[0])):
            if data[rowid][colid] == ">":
                face_right[(rowid, colid)] = True
            elif data[rowid][colid] == "v":
                face_down[(rowid, colid)] = True

    should_stop = False
    iter = 0
    while not should_stop:
        print(iter)
        should_stop = True
        iter += 1
        face_right_copy = face_right.copy()
        face_down_copy = face_down.copy()
        for sea_cucumber_coord in face_right_copy:
            next_coord = (sea_cucumber_coord[0], (sea_cucumber_coord[1] + 1) % C)
            if next_coord not in face_right_copy and next_coord not in face_down_copy:
                face_right.pop(sea_cucumber_coord)
                face_right[next_coord] = True
                should_stop = False
        for sea_cucumber_coord in face_down_copy:
            next_coord = ((sea_cucumber_coord[0] + 1) % R, sea_cucumber_coord[1])
            if next_coord not in face_right and next_coord not in face_down_copy:
                face_down.pop(sea_cucumber_coord)
                face_down[next_coord] = True
                should_stop = False

    #showMap(R, C, face_right, face_down)
    return iter


def main():
    data = open("input.txt").read().strip().split("\n")

    sol1 = func(data)
    print(f"Solution 1: {sol1}")


if __name__ == "__main__":
    main()
