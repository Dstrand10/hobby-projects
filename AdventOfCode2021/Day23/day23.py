#PART 1
total = 0
#############
#...........#
###D#B#D#A###
  #C#C#A#B#
  #########

total += 8 + 30 + 5000 + 8000
#############
#.A.......B.# 8 + 30 + 5000 + 8000
###.#B#.#D###
  #C#C#A#D#
  #########

total += 3 + 20
#############
#.A.B...A.B.# 3 + 20
###.#.#.#D###
  #C#C#.#D#
  #########

total += 600 + 30
#############
#.A.....A.B.# 600 + 30
###.#.#.#D###
  #C#B#C#D#
  #########

total += 700 + 3 + 6 + 60
#############
#...........# 700 + 3 + 6 + 60
###B#B#C#D###
  #A#B#C#D#
  #########

print(f"Solution 1: {total}")


#PART 2

total = 0
#############
#...........#
###D#B#D#A###
  #D#C#B#A#
  #D#B#A#C#
  #C#C#A#B#
  #########

total += 9 + 9 + 500 + 50
#############
#AA.......BC# 9 + 9 + 500 + 50
###D#B#D#.###
  #D#C#B#.#
  #D#B#A#.#
  #C#C#A#.#
  #########

total += 7000 + 10000 + 10000 + 10000 + 900
#############
#AA.....C.BC# 7000 + 10000 + 10000 + 10000 + 900
###.#B#.#D###
  #.#C#B#D#
  #.#B#A#D#
  #.#C#A#D#
  #########

total += 5 + 5 + 70
#############
#.B.....C.BC# 5 + 5 + 70
###.#B#.#D###
  #.#C#.#D#
  #A#B#A#D#
  #A#C#A#D#
  #########

total += 9 + 9 + 500
#############
#.B.......BC# 9 + 9 + 500
###A#B#.#D###
  #A#C#.#D#
  #A#B#.#D#
  #A#C#C#D#
  #########

total += 20 + 700 + 60 + 800
#############
#.B.B...B.BC# 20 + 700 + 60 + 800
###A#.#.#D###
  #A#.#C#D#
  #A#.#C#D#
  #A#.#C#D#
  #########

total += 50 + 60 + 50 + 60 + 500
#############
#...........# 50 + 60 + 50 + 60 + 500
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

print(f"Solution 2: {total}")