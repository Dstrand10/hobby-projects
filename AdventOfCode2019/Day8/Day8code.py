import numpy as np
from matplotlib import pyplot as plt

################## CODE Part 1 #########################################################################################
file = open("Day8input", "r")
content = str(file.read())

layerWidth = 25
layerHeight = 6
totalPixelsPerLayer = layerHeight * layerWidth

layerNbr = None
layerWithMinZeros = None
minNbrOf0s = totalPixelsPerLayer + 1
value1sTimes2s = None

for countOfLayer in range(int(len(content) / totalPixelsPerLayer)):
    layer = content[countOfLayer * totalPixelsPerLayer:(countOfLayer + 1) * totalPixelsPerLayer]
    countZeros = 0
    counted1s = 0
    counted2s = 0
    for char in layer:
        if char == "0":
            countZeros += 1
        elif char == "1":
            counted1s += 1
        elif char == "2":
            counted2s += 1
    if countZeros < minNbrOf0s:
        layerWithMinZeros = layer
        layerNbr = countOfLayer
        minNbrOf0s = countZeros
        value1sTimes2s = counted1s * counted2s

# print("Layer Number:")
# print(layerNbr)
# print("The final layer:")
# print(layerWithMinZeros)
# print("Number of zeros:")
# print(minNbrOf0s)
print("The amount of counted 1's times counted 2's:")
print(value1sTimes2s)

########################### Part 2 ####################################################################################
indexToPaint = list(
    map(str, range(totalPixelsPerLayer)))  # As string to easier track what indexes that have been painted
picture = np.ones(totalPixelsPerLayer) * -1
layers = []

# Getting all layers separately
for countOfLayer in range(int(len(content) / totalPixelsPerLayer)):
    layers.append(content[countOfLayer * totalPixelsPerLayer:(countOfLayer + 1) * totalPixelsPerLayer])

paintedIndexes = []  # Keeping track of what indexes that have been painted

for layer in layers:
    for index in indexToPaint:
        if layer[int(index)] != "2" and index not in paintedIndexes:
            picture[int(index)] = int(layer[int(index)])  # Paints all the pixels that has a specified colour and already has not been painted yet
            paintedIndexes.append(str(index)) # Saves all painted pixels, so they can't be painted again

        # All pixels have been painted here
        if len(paintedIndexes) == len(indexToPaint):
            break

#Checking so all pixels have changed to a colour
if -1 in picture:
    print("Something went wrong, some pixel has not been painted. Look at the picture")
    print(picture)

#Plotting the picture
plt.imshow(np.reshape(picture, [layerHeight, layerWidth]))
plt.show()