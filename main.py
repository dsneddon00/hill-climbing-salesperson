#! /usr/bin/env python3
import random
import time

'''
 _____ ___________   _   _ _ _ _   _____ _ _           _
|_   _/  ___| ___ \ | | | (_) | | /  __ \ (_)         | |
  | | \ `--.| |_/ / | |_| |_| | | | /  \/ |_ _ __ ___ | |__   ___ _ __
  | |  `--. \  __/  |  _  | | | | | |   | | | '_ ` _ \| '_ \ / _ \ '__|
  | | /\__/ / |     | | | | | | | | \__/\ | | | | | | | |_) |  __/ |
  \_/ \____/\_|     \_| |_/_|_|_|  \____/_|_|_| |_| |_|_.__/ \___|_|

______        ______              _      _____                _     _
| ___ \       |  _  \            | |    /  ___|              | |   | |
| |_/ /_   _  | | | |___ _ __ ___| | __ \ `--. _ __   ___  __| | __| | ___  _ __
| ___ \ | | | | | | / _ \ '__/ _ \ |/ /  `--. \ '_ \ / _ \/ _` |/ _` |/ _ \| '_ \
| |_/ / |_| | | |/ /  __/ | |  __/   <  /\__/ / | | |  __/ (_| | (_| | (_) | | | |
\____/ \__, | |___/ \___|_|  \___|_|\_\ \____/|_| |_|\___|\__,_|\__,_|\___/|_| |_|
        __/ |
       |___/

'''

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

# grabbing whatever length of the route is and returning it to the user
# tasks in a full tsp mapping and a solution
def getUtility(tsp, s):
    utility = 0
    for i in range(len(s)):
        # we are working with lists within lists, which is why we need the [s[i]]
        utility += tsp[s[i - 1]][s[i]]
    return utility

# essentially create a solution by taking all of the previous solution and swapping all of neighbors (we must ensure that we visit every part of the solution)
def generateNeighboringSolution(s):
    nList = []
    # for each neighbor pair set...
    for i in range(len(s)):
        # we need an offset of i + 1 so we get the one next to i and keep it within the solution
        for j in range(i + 1, len(s)):
            # remember the neighboring solution must be idential to the initial solution at first
            n = s.copy()
            # swappy time
            n[i] = s[j]
            n[j] = s[i]
            # slapped the swapped node back onto to nList
            nList.append(n)
    return nList

# we generate neighbors until we find the best one an update the user with its utility
def findBestNeighbor(tsp, nList):
    # setting defaults
    uBest = getUtility(tsp, nList[0])
    nBest = nList[0]
    # run the utility calculations on all the neighbors and basically do a classic
    # code grinder min of list function
    for n in nList:
        curU = getUtility(tsp, n)
        # min checking, keep default
        if curU < uBest:
             uBest = curU
             nBest = n
    # returning a tuple of the best utility and the neighbor
    return nBest, uBest



# takes in the data of an a string, splits it, and returns how many actually numbers there are
def getTotalNumbers(numberString):
    total = 0
    for item in numberString.split():
        #print(item)
        total += 1
    return total

def prepListForCalcuations(intList):
    newList = []
    for i in range(len(intList)):
        innerList = []
        for item in intList[i].split():
            innerList.append(int(item))
        newList.append(innerList)

    return newList

def main():
    # activate timer
    start = time.time()

    currentList = readTSPData(input("Please input a filename: "))
    #printListValuesWithIndexAndLength(currentList)
    currentList = prepListForCalcuations(currentList)
    #print(currentList)
    # okay let's test the shuffle
    currentS = generateRandomState(currentList)
    #print(currentS)
    #print("length for checking: " + str(len(currentList)))
    #print("Utility of random:", getUtility(currentList, currentS))
    currentU = getUtility(currentList, currentS)
    nList = generateNeighboringSolution(currentS)

    resultingN, resultingU = findBestNeighbor(currentList, nList)

    # actuall hill climbing search here
    # look for the smallest minimum utility
    while(resultingU < currentU and (time.time() - start <= 120)):
        currentS = resultingN
        currentU = resultingU
        # set the neighbor list to the appropriate solution
        nList = generateNeighboringSolution(currentS)
        # run through getting the best neighbor again
        resultingN, resultingU = findBestNeighbor(currentList, nList)
        print("Current Neighboring Solution:", str(resultingN))
        print("Current Utility:", str(resultingU))

    print("Utility:", currentU)
    print("Time it took:", str(time.time() - start))


    return

if __name__ == "__main__":
    main()



# Guidelines for this assignment:
#   - Recasting the TSP problem as a hill climbing one
#   - Initial State = random ordering of all cities with home city typically first
#   - Nieghbor = swap 2 city locations
#       -- n(n-1) = n^2
#   - DON'T CALCULATE DISTANCES
