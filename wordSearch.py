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
import re
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

myWords = inputWords()
print(myWords)