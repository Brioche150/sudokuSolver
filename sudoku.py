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
            if grid[r][c] !=0 and type(grid[r][c]) != set:
                #print(grid[r][c]," is in area")
                missingNums.remove(grid[r][c])
            #else:
                #print(" Nothing here")
    #print(missingNums)
    return missingNums

def elimination(r,c, possibleNums):
    
    for i in range(gridLength):
        if grid[i][c] in possibleNums:
            possibleNums.remove(grid[i][c])
        if grid[r][i] in possibleNums:
            possibleNums.remove(grid[r][i])
    return possibleNums

def reduceOptions(r,c, possibleNums):
            
    if type(grid[r][c]) == set:
        possibleNums = list(grid[r][c])
    else:
        possibleNums = missingNums.copy() #
    possibleNums = elimination(r,c,possibleNums)
    for target in possibleNums:
        if ((target,c) in confirmedNumInCol and confirmedNumInCol[(target,c)] != areaNum) or ((target,r) in confirmedNumInRow and confirmedNumInRow[(target,r)] != areaNum): # Under these conditions you can't do think the number is there
            #This is in the case that it is trying to find a space for a number. If there is confirmed a number in that row or column, then that number can't be placed here. The areaNum is to check that it isn't marking a confirmed one in the area, and stop assignments.
            possibleNums.remove(target)
    return possibleNums

def findPossibilities(areaNum, eliminate= False):
    positions = {}
    possibleNums =[]
    for i in missingNums:
        positions.update({i:[]})
    isUpdated = False
    rowStart = int(areaLength * int(areaNum/areaLength))
    colStart = areaLength * (areaNum%areaLength)
    for r in range(rowStart,rowStart + areaLength):
        for c in range(colStart, colStart + areaLength):
            if grid[r][c] not in range(1,gridLength+1): # used to be if grid[r][c] == 0, but I have to account for sets now
                possibleNums = reduceOptions(r,c,possibleNums)
                        
                if eliminate and len(possibleNums) ==1:
                    grid[r][c] = possibleNums[0]
                    if grid[r][c] in missingNums: #This was breaking it if an elimination happened while doing the other square method
                        missingNums.remove(grid[r][c])
                        positions.pop(grid[r][c])
                    # print("AreaNum:", areaNum, "Elimination: filled at row", r, "Column", c)
                    # printGrid()
                    isUpdated = True
                    
                else:
                    for i in possibleNums: #So if that number never turned up, then add that number and its coordinates to the dictionary.
                            positions[i].append((r,c))

    if eliminate: return positions, isUpdated
    else: return positions

grid = [
    [0,0,0,0,3,4,8,0,0],
    [8,0,4,6,0,0,0,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,0,0,5,0,0,6,0,0],
    [0,4,0,7,0,9,0,3,0],
    [0,0,3,0,0,8,0,0,9],
    [0,0,0,0,7,0,3,2,0],
    [0,2,6,0,0,1,9,0,5],
    [0,0,7,9,2,0,0,0,4]
]
'''
solution to grid = [
    [0,0,0,0,3,4,8,0,0],
    [8,0,4,6,0,0,0,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,0,0,5,0,0,6,0,0],
    [0,4,0,7,0,9,0,3,0],
    [0,0,3,0,0,8,0,0,9],
    [0,0,0,0,7,0,3,2,0],
    [0,2,6,0,0,1,9,0,5],
    [0,0,7,9,2,0,0,0,4]
]
is  [
    [7,6,5,1,3,4,8,9,2],
    [8,1,4,6,9,2,7,5,3],
    [2,3,9,8,5,7,4,1,6],
    [1,9,2,5,4,3,6,8,7],
    [5,4,8,7,6,9,2,3,1],
    [6,7,3,2,1,8,5,4,9],
    [9,5,1,4,7,6,3,2,8],
    [4,2,6,3,8,1,9,7,5],
    [3,8,7,9,2,5,1,6,4]
] 
'''

 

gridLength = len(grid)
printGrid()

areaLength = int(math.sqrt(gridLength))
updatedByScanning = True
#This will store the number, the row/column that the number is in, and the area number it is in
confirmedNumInRow = {}
confirmedNumInCol = {}
gridUpdated = True
while gridUpdated:
    gridUpdated = False
    while updatedByScanning:
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
    
    incomplete = [True for row in grid if 0 in row]
    if incomplete:
        prevConfirmedNumInCol = confirmedNumInCol.copy()
        prevConfirmedNumInRow = confirmedNumInRow.copy()
        nakedPairs = {}
        for areaNum in range(gridLength):
            numInRow = {}
            numInCol = {}
            missingNums = targetSearch(areaNum) 
            positions  = findPossibilities(areaNum)
            
            nums = list(positions.keys()) # Needed for the pairs/ n-lets
             # nakedPairs will make a dictionary of all coordinate sets, and the numbers which have them. 
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
                
                ''' Now I need to do things with naked pairs or maybe n-lets
                How to figure this?
                Look at the possible locations for each number. This will be a list of coordinates. Might have to make it a set of coordinates to be able to compare them better
                One way is to compare every number with every other number, look at their sets of coords, see if they match up (may have to check if it's IN, rather than equal another number's set). 
                If they do match up, put a set of those numbers into those grid coordinates, and have a check for everything else, so basically the program can't try to put any other number in there.
                How to do triplets and higher/ recognise multiple pairs in a pass? When matching coords are found, add it to a list, then for every other number, check it against that list first, if not, then go through the other numbers looking for it 
                Once I identify naked pairs/n-lets, put that set of numbers into a grid location, instead of just a number, and for every other comparison, do if num in grid[r][c] 
                There are scenarios where two numbers will have the same possible coordinates, and another number shares 2 of them
                '''
                if not tuple(positions[num]) in nakedPairs:
                    temp = set()
                    temp.add(num)
                    nakedPairs[tuple(positions[num])] = temp
                tempNums = nums.copy()
                for otherNum in tempNums:
                    if num == otherNum:
                        nums.remove(num)
                    elif len(positions[num]) ==2 and positions[num] == positions[otherNum]: # This is looking to see if there is an entry with a key of two coordinates, with two different numbers that can only go in those coordinates.
                        nakedPairs[tuple(positions[num])].add(otherNum)
                                
            #Now to deal with the nakedPairs. If there is a set of coordinates that multiple numbers can go to, then they will be a naked n-let.
            #This set of numbers will be put into the grid, so that the only numbers that can occupy that spot are ones in that set
            
            
        for coords in nakedPairs:
            if len(nakedPairs[coords]) > 1:
                for coord in coords:
                    if(grid[coord[0]][coord[1]] != nakedPairs[coords]):
                        grid[coord[0]][coord[1]] = nakedPairs[coords]
                        updatedByScanning = gridUpdated = True
                
        if prevConfirmedNumInCol != confirmedNumInCol  or prevConfirmedNumInRow != confirmedNumInRow: 
            updatedByScanning = gridUpdated = True
            #NumInRow and Col determines if certain numbers only fit in a certain row or column,as if that is the case, the length of the set will be 1

        # this finds naked pairs in rows
        
        areaNum = -1
        possibleNums = []
        nakedPairs = {}
        
        for row in range(gridLength):
            positions = {}
            
            for col in range(gridLength):
                tempAreaNum = int(row / areaLength) * areaLength + int(col / areaLength)
                if areaNum != tempAreaNum:
                    areaNum = tempAreaNum
                    missingNums = targetSearch(areaNum)
                    for i in missingNums:
                        if not i in positions:
                            positions.update({i:[]})
                            
                if grid[row][col] not in range(1,gridLength+1): 
                    possibleNums = reduceOptions(row,col,possibleNums)
                    for i in possibleNums: #So if that number never turned up, then add that number and its coordinates to the dictionary.
                        positions[i].append((row,col))
        
            nums = list(positions.keys())
            for num in positions:        
                    if not tuple(positions[num]) in nakedPairs: # the coordinates are the key, 
                        temp = set()
                        temp.add(num)
                        nakedPairs[tuple(positions[num])] = temp
                    tempNums = nums.copy()
                    for otherNum in tempNums:
                        if num == otherNum:
                            nums.remove(num)
                        elif len(positions[num]) ==2 and positions[num] == positions[otherNum]:
                            nakedPairs[tuple(positions[num])].add(otherNum)
        
        # Now to find naked pairs in the columns. I don't have to clear naked pairs since they can't possibly make the same coordinate pairs
        areaNum = -1
        possibleNums = []
        positions = {}
        for col in range(gridLength):
            positions = {}
            
            for row in range(gridLength):
                tempAreaNum = int(row / areaLength) * areaLength + int(col / areaLength)
                if areaNum != tempAreaNum:
                    areaNum = tempAreaNum
                    missingNums = targetSearch(areaNum)
                    for i in missingNums:
                        if not i in positions:
                            positions.update({i:[]})
                            
                if grid[row][col] not in range(1,gridLength+1): 
                    possibleNums = reduceOptions(row,col,possibleNums)
                    for i in possibleNums: #So if that number never turned up, then add that number and its coordinates to the dictionary.
                        positions[i].append((row,col))
        
            nums = list(positions.keys())
            for num in positions:        
                    if not tuple(positions[num]) in nakedPairs: # the coordinates are the key, 
                        temp = set()
                        temp.add(num)
                        nakedPairs[tuple(positions[num])] = temp
                    tempNums = nums.copy()
                    for otherNum in tempNums:
                        if num == otherNum:
                            nums.remove(num)
                        elif len(positions[num]) ==2 and positions[num] == positions[otherNum]:
                            nakedPairs[tuple(positions[num])].add(otherNum)
        for coords in nakedPairs:
            if len(nakedPairs[coords]) > 1:
                for coord in coords:
                    if(grid[coord[0]][coord[1]] != nakedPairs[coords]):
                        grid[coord[0]][coord[1]] = nakedPairs[coords]
                        updatedByScanning = gridUpdated = True
                        
        printGrid()
        