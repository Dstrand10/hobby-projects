# FIX THIS SPAGHETTI

def padImage(image_input, img_enh, iter):

    padder = "#" if img_enh[0] == "#" and img_enh[1] == "." and iter % 2 == 1 else "."
    C = len(image_input[0])

    padded_image = []
    padded_image.extend([padder*(C+6)] * 3)
    for row in image_input:
        padded_image.append(3*padder + row + 3*padder)
    padded_image.extend([padder * (C + 6)] * 3)
    return padded_image


def convertTodecimal(imageWindow):
    bin = ""
    for x in imageWindow:
        if x == ".":
            bin += "0"
        else:
            bin += "1"
    return int(bin, 2)


def printImage(outputImage):
    print("--- Image printed below ---")
    for row in outputImage:
        print(row)
    print("--- Image printed above ---")


def cutOutputImage(outputImage):
    new_output = []
    for row in outputImage[1:-1]:
        new_output.append(row[1:-1])
    return new_output


def func(data, iter):
    image_enhancement = data[0].strip().replace("\n", "")

    image_input = data[1].split("\n")
    #printImage(image_input)
    for i in range(iter):
        paddedImage = padImage(image_input, (image_enhancement[0], image_enhancement[-1]), i)
        #printImage(paddedImage)
        outputImage = []
        outputImage.extend(["."*len(paddedImage[0])] * len(paddedImage))
        for rowid in range(1, len(paddedImage) - 1):
            for colid in range(1, len(paddedImage[0]) - 1):
                imageWindow = [item for sublist in [x[colid-1:colid+2] for x in paddedImage[rowid-1:rowid+2]] for item in sublist]
                dec = convertTodecimal(imageWindow)
                if image_enhancement[dec] == "#":
                    outputImage[rowid] = outputImage[rowid][:colid] + "#" + outputImage[rowid][colid+1:]
        #printImage(outputImage)
        #printImage(cutOutputImage(outputImage))
        image_input = cutOutputImage(outputImage)
    total_lit = 0
    for row in outputImage:
        total_lit += row.count("#")
    return total_lit

def func2(data):
    pass


def main():
    data = open("input.txt").read().split("\n\n")




    sol1 = func(data, 2)
    print(f"Solution 1: {sol1}")

    sol2 = func(data, 50)
    print(f"Solution 2: {sol2}")


if __name__ == "__main__":
    main()
