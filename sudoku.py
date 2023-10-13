import math
def printGrid():
    for row in grid:
        print(row)
    print()

#changing this to just return a list of which numbers isn't in the area, because that just makes this faster
def targetSearch(areaNum): # Area num has to be 0 indexed for the integer division to work
    # the row number of the area will start at the area length * the number of rows down
    missingNums = [i for i in range(1, gridLength +1)]
    rowStart = int(areaLength * int(areaNum/areaLength))
    colStart = areaLength * (areaNum%areaLength)
    for r in range(rowStart,rowStart + areaLength):
        for c in range(colStart, colStart + areaLength):
            #print("Checking row:", r, "and column:", c, end=" ")
            if grid[r][c] != 0:
                #print(grid[r][c]," is in area")
                missingNums.remove(grid[r][c])
            #else:
                #print(" Nothing here")
    #print(missingNums)
    return missingNums

def findPossibilitiesAndElimination(areaNum):
    positions = {}
    for i in missingNums:
        positions.update({i:[]})
    isUpdated = False
    targetsFound = []
    rowStart = int(areaLength * int(areaNum/areaLength))
    colStart = areaLength * (areaNum%areaLength)
    for r in range(rowStart,rowStart + areaLength):
        for c in range(colStart, colStart + areaLength):
            if grid[r][c] == 0:
                targetsFound = [False for i in range(len(missingNums))]
                possibleNums = [i for i in range(1, gridLength+1)]
                for i in range(gridLength): #When this wasn't doing all of the numbers in one go, I could've made this a while, stopping if the target was found. Now, though, that would be a similar amount of iterating, if not more
                    if grid[i][c] in possibleNums:
                        possibleNums.remove(grid[i][c])
                    if grid[r][i] in possibleNums:
                        possibleNums.remove(grid[r][i])
                    j =0
                    for target in missingNums:
                        if grid[i][c] == target: targetsFound[j] = True
                        if grid[r][i] == target: targetsFound[j] = True
                        j+=1
                if len(possibleNums) ==1:
                    grid[r][c] = possibleNums[0]
                    if grid[r][c] in missingNums: #This was breaking it if an elimination happened while doing the other square method
                        missingNums.remove(grid[r][c])
                        positions.pop(grid[r][c])
                    # print("AreaNum:", areaNum, "Elimination: filled at row", r, "Column", c)
                    # printGrid()
                    
                    isUpdated = True
                else:
                    for i in range(len(targetsFound)): #So if that number never turned up, then add that number and its coordinates to the dictionary.
                        if not targetsFound[i]:
                            positions.get(missingNums[i]).append([r,c])

                
    #print(positions)
    return positions, isUpdated

grid = [
    [7,0,0,0,3,4,8,0,0],
    [8,0,4,6,0,0,0,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,0,0,5,0,0,6,0,0],
    [0,4,0,7,0,9,0,3,0],
    [0,0,3,0,0,8,0,0,9],
    [0,0,0,0,7,0,3,2,0],
    [0,2,6,0,0,1,9,0,5],
    [0,0,7,9,2,0,0,0,4]
]
gridLength = len(grid)
printGrid()

areaLength = int(math.sqrt(gridLength))
updatedByScanning = True
positions ={}
while updatedByScanning:
    updatedByScanning = False  
    for areaNum in range(gridLength):
        missingNums = targetSearch(areaNum)
        if missingNums: # empty lists give a 0 value that can be read as false for truth statements
            positions, isUpdated = findPossibilitiesAndElimination(areaNum)
            if isUpdated:
                updatedByScanning = True
            for num in positions:
                if len(positions.get(num)) == 1:
                    row, column = positions.get(num)[0][0], positions.get(num)[0][1]
                    grid[row][column] = num
                    # print("AreaNum:", areaNum, "Square method at row",row,"Column",column)
                    # printGrid()
                    
                    updatedByScanning = True
    printGrid()
#I'm going to put all of the possible positions in the coordinates, rather than just a number
incomplete = [False for row in grid if R[]]
if incomplete:
    for areaNum in range(gridLength):

    