from Intcode import Intcode




input = list(map(int, open("inputdata_2", "r").readline().split(",")))
inten = Intcode()
inten.readCode(input)