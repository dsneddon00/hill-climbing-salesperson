import random

# given a list of tsp locations, scramble them and return that
def generateInitialState(tspList):

    result = []
    # creating nodes for each of the coordinate sets
    nodeList = list(range(len(tspList)))

    for i in range(len(tspList)):
        cur = nodeList[random.randint(0, len(noeList) - 1)]
        result.append(cur)
        # we have added a random node, now we must remove the identical one
        # from our node list
        nodeList.remove(cur)

    return result












def readTSPData(filename):
    with open("data/" + filename) as fout:
        print(fout.readlines())

def main():
    readTSPData(input("Please input a filename: "))
    return

if __name__ == "__main__":
    main()



# Guidelines for this assignment:
#   - Recasting the TSP problem as a hill climbing one
#   - Initial State = random ordering of all cities with home city typically first
#   - Nieghbor = swap 2 city locations
#       -- n(n-1) = n^2
#   - DON'T CALCULATE DISTANCES
