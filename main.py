#! /usr/bin/env python3
import random

# given a list of tsp locations, scramble them and return that
def generateRandomState(tspList):

    result = []
    # creating nodes for each of the coordinate sets
    nodeList = list(range(len(tspList)))

    for i in range(len(tspList)):
        cur = nodeList[random.randint(0, len(nodeList) - 1)]
        result.append(cur)
        # we have added a random node, now we must remove the identical one
        # from our node list
        nodeList.remove(cur)

    return result









# Helper built to remove any endline characters
def cleanIntList(intList):
    for item in intList:
        if item == "\n":
            intList.remove(item)
    return intList

def readTSPData(filename):
    fout = open("data/" + filename, "r")
    #with open("data/" + filename) as fout:
    #    newList = cleanIntList(fout.readlines())
    resultingList = []
    #print(newList)
    for line in fout:
        # when it reaches this stage, it's currently a list of strings
        line = line.strip()
        resultingList.append(line)
    return resultingList

        #print(fout.readlines())

def printListValuesWithIndexAndLength(intList):
    for i in range(len(intList)):
        print(str(i) + ": " + str(intList[i]) + " Length: " + str(getTotalNumbers(intList[i])) + "\n")

# takes in the data of an a string, splits it, and returns how many actually numbers there are
def getTotalNumbers(numberString):
    total = 0
    for item in numberString.split():
        #print(item)
        total += 1
    return total

def main():
    currentList = readTSPData(input("Please input a filename: "))
    printListValuesWithIndexAndLength(currentList)
    return

if __name__ == "__main__":
    main()



# Guidelines for this assignment:
#   - Recasting the TSP problem as a hill climbing one
#   - Initial State = random ordering of all cities with home city typically first
#   - Nieghbor = swap 2 city locations
#       -- n(n-1) = n^2
#   - DON'T CALCULATE DISTANCES
