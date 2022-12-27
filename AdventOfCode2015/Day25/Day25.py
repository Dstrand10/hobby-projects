codes = {(1, 1): 20151125}
lastCoord = None
coord = (1, 1)

while True:
    if coord not in codes:
        codes[coord] = (codes[lastCoord] * 252533) % 33554393
    if coord == (3010, 3019):
        print(codes[coord])
        break
    lastCoord = coord
    coord = (coord[0] - 1, coord[1] + 1)
    if coord[0] < 1:
        coord = (coord[1], 1)
