import math
def targetSearch(target, areaNum): # Area num has to be 0 indexed for the integer division to work
    print("Searching for:", target, "in area number", areaNum)
    # the row number of the area will start at the area length * the number of rows down
    rowStart = int(areaLength * int(areaNum/areaLength))
    colStart = areaLength * (areaNum%areaLength)
    for r in range(rowStart,rowStart + areaLength):
        for c in range(colStart, colStart + areaLength):
            print("Checking row:", r, "and column:", c, end=" ")
            if grid[r][c] == target:
                print(" Target is in area")
            else:
                print(" Not here")

grid = [
    [0,0,0,1],
    [0,2,0,0],
    [0,0,4,0],
    [3,0,0,0]
]
gridLength = len(grid)
# for row in grid:
#     print(row)
areaLength = int(math.sqrt(gridLength))
for i in range(4):
    targetSearch(1,i)

