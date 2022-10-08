import numpy as np

file = open("Day6input", "r")

if file.mode == "r":
    content = file.read()
    orbits = content.splitlines()

allSpaceObjects = ["COM"]
for orbit in orbits:
    spaceObjects1 = orbit.split(")")
    SO1 = spaceObjects1[0]
    SO2 = spaceObjects1[1]

    if SO1 not in allSpaceObjects:
        allSpaceObjects.append(SO1)
    if SO2 not in allSpaceObjects:
        allSpaceObjects.append(SO2)


def createDirectedAdjacencyMatrix():
    adjMatrix = np.zeros((len(allSpaceObjects), len(allSpaceObjects)))
    for orbit in orbits:
        spaceObjects2 = orbit.split(")")
        index1 = allSpaceObjects.index(spaceObjects2[0])
        index2 = allSpaceObjects.index(spaceObjects2[1])
        adjMatrix[index1][index2] = 1
    return adjMatrix


def createUndirectedAdjacencyMatrix():
    adjMatrix = np.zeros((len(allSpaceObjects), len(allSpaceObjects)))
    for orbit in orbits:
        spaceObjects2 = orbit.split(")")
        index1 = allSpaceObjects.index(spaceObjects2[0])
        index2 = allSpaceObjects.index(spaceObjects2[1])
        adjMatrix[index1][index2] = 1
        adjMatrix[index2][index1] = 1
    return adjMatrix


def calculateOrbitsFromAdjacencyMatrix(adjMatrix):
    countSO = np.count_nonzero(adjMatrix[:1])
    nbrOfIndividualOrbits = 1
    totalOrbits = countSO * nbrOfIndividualOrbits
    print(totalOrbits)
    g = adjMatrix
    while countSO > 0:
        g = np.matmul(g, adjMatrix)
        countSO = np.count_nonzero(g[:1])
        nbrOfIndividualOrbits += 1
        totalOrbits += countSO * nbrOfIndividualOrbits
        print(totalOrbits)


def calculateOrbitsBetweenTwoSpaceObjects(undirectedAdjMatrix, spaceObject1, spaceObject2):
    SO1index = allSpaceObjects.index(spaceObject1)
    SO2index = allSpaceObjects.index(spaceObject2)
    g = undirectedAdjMatrix
    isConnected = undirectedAdjMatrix[SO1index][SO2index]
    count = 1
    if isConnected > 0:
        return count
    while True:
        g = np.matmul(g, undirectedAdjMatrix)
        count += 1
        isConnected = g[SO1index][SO2index]
        if isConnected > 0:
            return count
        if count > 10000:
            print("Too many iterations, check it out.")
            break




# adjacencyMatrix = createDirectedAdjacencyMatrix(orbits)
# print(adjacencyMatrix)
# print(calculateOrbitsFromAdjacencyMatrix(adjacencyMatrix))

undirectedAdjMatrix = createUndirectedAdjacencyMatrix()
print(calculateOrbitsBetweenTwoSpaceObjects(undirectedAdjMatrix, "YOU", "SAN") - 2) #Answer part 2, minus 2 because YOU and SAN vertices should not be counted
