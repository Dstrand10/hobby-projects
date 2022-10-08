from Intcode import Intcode

input = list(map(int, open("inputdata_day2_1", "r").readline().split(",")))
inten = Intcode()
result = inten.readCode(input)
print(result[0])

input = list(map(int, open("inputdata_day2_1", "r").readline().split(",")))
for i in range(99):
    for j in range(99):
        tmp_input = input.copy()
        tmp_input[1] = i
        tmp_input[2] = j
        if Intcode().readCode(tmp_input)[0] == 19690720:
            print(i*100+j)