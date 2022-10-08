from Intcode import Intcode

input = list(map(int, open("input.txt", "r").readline().split(",")))

intcode = Intcode().setMemory(input)
intcode.readCode()
