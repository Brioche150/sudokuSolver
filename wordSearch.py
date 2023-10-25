'''
plan for making a  word search algorithm.
Get the list of words, and put them into a list
place the words on a grid. Do this by choosing a random space for a word, and checking if it can be put in a random orientation. I could basically number compass directions.
If it can't be placed in that direction, go around the compass and keep checking if it's possible. If it isn't, choose another random spot.
Do this for the next word. Make sure that words can share letters by only making a space unavailable if there is a letter in a position where that word would place a different one.
Once this is done, go through the whole grid, and place random letters for any unfilled cells.

Store where each word starts and what direction it goes in.
Then, print the grid and show the words to guess.
When they guess it right, change the letters to capitals or some other signifier.
'''
import re, random
def wordList():
    return ["happy", "cheerful", "chipper", "effervescent", "jaunty", "jolly"]

def inputWords():
    words = []
    isEntering = True
    while(isEntering):
        word = input("Please enter a word. If you would like to stop, then just hit enter: ")
        if(word == ""):
            isEntering = False
        elif re.search("[^a-zA-Z]", word):
            print("Please only input characters in the alphabet. It gets too easy otherwise.")
        else:
            words.append(word.lower())
    return words

def displayWords():
    for word in words:
        print(word, end =" ")
    print()

def printGrid():
    for row in grid:
        print("[", end =" ")
        for item in row:
            print(item, end = " ")
        print("]", end =" ")
        print()
    print("\n\n")

def generateGrid():
    height = width =0
    while(height < longestLength):
        height = int(input("Please enter the height of the grid you would like: "))
        if(height < longestLength):
            print("The height must be greater than or equal to the length of the longest word in the list.")
    while(width < longestLength):
        width = int(input("Please enter the width of the grid you would like: "))
        if(width < longestLength):
            print("The width must be greater than or equal to the length of the longest word in the list.")
    grid =[[" "] * width for i in range(height)]
    return grid

def wordWIllFit(col, row, word, direction):
    # 1 will go right, 2 down, 3 left, 4 up
    match direction:
        case 1:
            for i in range(len(word)):
                if col + i >= width or (grid[row][col +i] != word[i] and grid[row][col +i] != " "):
                    return False
        case 2:
            for i in range(len(word)):
                if row + i >= height or (grid[row+i][col] != word[i] and grid[row+i][col] != " "):
                    return False
        case 3:
            for i in range(len(word)):
                if col - i < 0 or (grid[row][col -i] != word[i] and grid[row][col -i] != " "):
                    return False
        case 4:
            for i in range(len(word)):
                if row - i < 0 or (grid[row-i][col] != word[i] and grid[row-i][col] != " "):
                    return False
    return True
def placeWord(word):
    wordFits = False
    while not wordFits: 
        col = random.randint(0, width -1)
        row = random.randint(0, height -1)
        direction = random.randint(1,4)
        wordFits = wordWIllFit(col,row,word, direction)
    match direction:
        case 1:
            for i in range(len(word)):
                grid[row][col +i] = word[i]
        case 2:
            for i in range(len(word)):
                grid[row+i][col] = word[i]
        case 3:
            for i in range(len(word)):
                grid[row][col -i] = word[i]
        case 4:
            for i in range(len(word)):
                grid[row-i][col] = word[i]
    
        

def placeWords():
    for word in words:
        placeWord(word)

words = wordList()
displayWords()
longestLength = 0
for word in words:
    if len(word) > longestLength:
        longestLength = len(word) 
grid = generateGrid()
height = len(grid)
width = len(grid[0])
printGrid()
placeWords()
printGrid()
print(height)
print(len(grid))