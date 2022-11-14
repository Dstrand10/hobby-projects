import itertools
import numpy


with open("input.txt") as f:
    ingredients = list()
    ingredient_matrix = numpy.zeros([4, 5])
    for idx, datarow in enumerate(f.readlines()):
        ingredient_matrix[idx][0] = int(datarow.split(" ")[2].replace(",", ""))
        ingredient_matrix[idx][1] = int(datarow.split(" ")[4].replace(",", ""))
        ingredient_matrix[idx][2] = int(datarow.split(" ")[6].replace(",", ""))
        ingredient_matrix[idx][3] = int(datarow.split(" ")[8].replace(",", ""))
        ingredient_matrix[idx][4] = int(datarow.split(" ")[10].replace(",", ""))

    maxScore = 0
    maxScoreCalories500 = 0
    #print(len(list(filter(lambda x: sum(x) == 100, itertools.product(range(100), repeat=4))))) #176847 possible distributions
    for distribution in filter(lambda x: sum(x) == 100, itertools.product(range(100), repeat=4)):
        dist_array = numpy.array(distribution)
        calculation = numpy.matmul(dist_array, ingredient_matrix)
        if not all([i >= 0 for i in calculation[:-1]]):
            continue
        current_score = numpy.prod(calculation[:-1])
        if current_score > maxScore:
            maxScore = current_score
        if int(calculation[-1]) == 500 and current_score > maxScoreCalories500:
            maxScoreCalories500 = current_score
    print("Answer 1: " + str(int(maxScore)))
    print("Answer 2: " + str(int(maxScoreCalories500)))
