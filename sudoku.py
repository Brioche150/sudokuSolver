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

def elimination(r,c, i, possibleNums):
    if grid[i][c] in possibleNums:
        possibleNums.remove(grid[i][c])
    if grid[r][i] in possibleNums:
        possibleNums.remove(grid[r][i])
    return possibleNums

def findPossibilities(areaNum, eliminate= False):
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
                if eliminate:
                    possibleNums = [i for i in range(1, gridLength+1)]
                for i in range(gridLength): #When this wasn't doing all of the numbers in one go, I could've made this a while loop, stopping if the target was found. Now, though, that would be a similar amount of iterating, if not more
                    if eliminate:
                        possibleNums = elimination(r,c,i,possibleNums)
                    
                    j =0
                    for target in missingNums:
                        if ((target,c) in confirmedNumInCol and confirmedNumInCol[(target,c)] != areaNum) or ((target,r) in confirmedNumInRow and confirmedNumInRow[(target,r)] != areaNum): # Under these conditions you can't do it
                            j+=1 #This is in the case that it is trying to find a space for a number. If there is confirmed a number in that row or column, then that number can't be placed here. The areaNum is to check that it isn't marking a confirmed one in the area, and stop assignments.
                            continue
                        else:
                            if grid[i][c] == target: 
                                targetsFound[j] = True
                            if grid[r][i] == target: targetsFound[j] = True
                        j+=1
                        
                if eliminate and len(possibleNums) ==1:
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
                            positions[missingNums[i]].append([r,c])


                
    #print(positions)
    if eliminate: return positions, isUpdated
    else: return positions

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
#This will store the number, the row/column that the number is in, and the area number it is in
confirmedNumInRow = {}
confirmedNumInCol = {}
gridUpdated = True
while gridUpdated:
    positions ={}
    gridUpdated = False
    while updatedByScanning:
        positions ={}
        updatedByScanning = False  
        for areaNum in range(gridLength):
            missingNums = targetSearch(areaNum)
            if missingNums: # empty lists give a 0 value that can be read as false for truth statements
                positions, isUpdated = findPossibilities(areaNum, eliminate=True)
                if isUpdated:
                    updatedByScanning = True
                for num in positions:
                    if len(positions[num]) == 1:
                        row, column = positions[num][0][0], positions[num][0][1]
                        grid[row][column] = num
                        confirmedNumInCol.pop((num,column), None) # This stops an error from coming up if the key isn't there, since it will only be there if brute force has failed
                        confirmedNumInRow.pop((num,row), None)
                        # print("AreaNum:", areaNum, "Square method at row",row,"Column",column)
                        # printGrid()
                        updatedByScanning = True
                        
        printGrid()
    #I'm going to put all of the possible positions in the coordinates, rather than just a number
    
    #Currently a bug of running forever if it gets here. Flags are being set to true when they shouldn't be.
    
    incomplete = [True for row in grid if 0 in row]
    if incomplete:
        prevConfirmedNumInCol = confirmedNumInCol.copy()
        prevConfirmedNumInRow = confirmedNumInRow.copy()
        for areaNum in range(gridLength):
            numInRow = {}
            numInCol = {}
            positions  = findPossibilities(areaNum)
            for num in positions: # So this loop will go through and make a list of every possible number that could go in each coordinate.
                numInRow.update({num:set()}) # Some lovely sets here, since a number could appear multiple times in the same row or column, and that would be the point of this detection system
                numInCol.update({num:set()})
                for coord in positions[num]:
                    row, column = coord[0], coord[1]
                    numInRow[num].add(row)
                    numInCol[num].add(column)
                if len(numInCol[num]) == 1:
                    confirmedNumInCol.update({(num, column): areaNum})
                if len(numInRow[num]) ==1:
                    confirmedNumInRow.update({(num,row): areaNum}) # would put numInRow[num].pop(), but if there's only one, then row has only been taking one value, and it's fine
        if prevConfirmedNumInCol != confirmedNumInCol  or prevConfirmedNumInRow != confirmedNumInRow: 
            updatedByScanning = gridUpdated = True
            #NumInRow and Col determines if certain numbers only fit in a certain row or column,as if that is the case, the length of the set will be 1
        
    