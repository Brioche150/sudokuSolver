'''
Pseudocode for hangman:
minLength <- input("Please give the minimum word length")
minLength <- input("Please give the maximum word length")
while len(word) < minLength or len(word) > maxLength
    word <- read random word from EnglishWords.txt
end while
wrongGuesses <- 6
answer = "-" * len(word)
while wrongGuesses > 0 and answer != word
    output("You have [wrongGuesses] left")
    letter <- first letter of input("Please enter a letter to guess") //take the first character
    for i in range(len(word))
        if letter == word[i]
            answer[i] = letter
            output("You guessed correctly")
        else
            wrongGuesses -=1
            output("You guessed incorrectly)
        end if
    end for
    output(answer)
end while
if answer == word
    output("Congratulations! You won")
else
    output("Unlucky. Better luck next time")
end if

This could all be wrapped in another while to let them go again
'''
import random
f = open("EnglishWords.txt")

words = f.readlines()
word = words[random.randint(0,len(words) -1)].strip()
wrongGuesses = 6
answer = "-" * len(word)
while wrongGuesses > 0 and answer != word:
    print("\nYou have %d wrong guesses left" % wrongGuesses)
    print("The word to guess is: " + answer)
    letter = input("Please guess a letter: ")[0].lower()
    temp = ""
    for i in range(len(word)):
        if letter == word[i]:
            temp += letter
        else:
            temp += answer[i]
            
    
    if(answer == temp):
        wrongGuesses -=1
        print("You guessed wrong")
    else:
        answer = temp
        print("Good Guess!")

if answer == word:
    print("Congratulations! You won!")
else:
    print("Unlucky, better luck next time.")
    print("The word was: " + word)