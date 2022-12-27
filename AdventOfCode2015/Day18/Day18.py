import numpy as np


def iterLights(current_lights):
    tmp_lights = np.zeros([len(current_lights), len(current_lights)])
    for row, lights in enumerate(current_lights):
        for col, light in enumerate(lights):
            row_start = row - 1
            row_stop = row + 2
            col_start = col - 1
            col_stop = col + 2
            if row_start < 0:
                row_start = 0
            if row_stop > len(current_lights):
                row_stop = row_stop - 1
            if col_start < 0:
                col_start = 0
            if col_stop > len(current_lights):
                col_stop = col_stop - 1
            nbr_lit_beside = sum(sum(current_lights[row_start:row_stop, col_start:col_stop])) - light

            if nbr_lit_beside == 3 or (light == 1 and nbr_lit_beside == 2):
                tmp_lights[row][col] = 1
    return tmp_lights


with open("input.txt") as f:
    data = f.readlines()
    lights_start = np.zeros([len(data), len(data)])

    for row, datarow in enumerate(data):
        for col, light in enumerate(datarow):
            if light == "#":
                lights_start[row][col] = 1

    current_lights_part1 = lights_start.copy()
    for i in range(100):
        current_lights_part1 = iterLights(current_lights_part1)
        #print(current_lights)
    print("Answer 1: " + str(int(sum(sum(current_lights_part1)))))

    current_lights_part2 = lights_start.copy()
    current_lights_part2[0][0] = 1
    current_lights_part2[0][-1] = 1
    current_lights_part2[-1][0] = 1
    current_lights_part2[-1][-1] = 1
    for i in range(100):
        current_lights_part2 = iterLights(current_lights_part2)
        current_lights_part2[0][0] = 1
        current_lights_part2[0][-1] = 1
        current_lights_part2[-1][0] = 1
        current_lights_part2[-1][-1] = 1
        # print(current_lights)
    print("Answer 2: " + str(int(sum(sum(current_lights_part2)))))
