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
'''
import random
hangmanStages = ['''
      +
      |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# ASCII art by Chris Horton, found on this github page: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

replay ="y"
while replay in ["y","Y","yes","Yes","YES"]:
    difficulty =0
    while difficulty <1 or difficulty >4:
        difficulty = int(input("Please choose the difficulty you would like\n1. Easy\n2. Medium\n3. Hard\n4. Customise word length\n"))
    maxLength = minLength =0
    match difficulty:
        case 1:
            minLength = 10
            maxLength = 9999
        case 2:
            minLength =6
            maxLength =9
        case 3:
            minLength =1
            maxLength =5
        case _:
            minLength = int(input("Please enter the minimum length of the word to guess: "))
            maxLength = int(input("Please enter the maximum length of the word to guess: "))
    
    words =[]
    with open("EnglishWords.txt") as f:
        for line in f:
            word = line.strip()
            if len(word) <= maxLength and len(word) >= minLength:
                words.append(word) 

    word = words[random.randint(0,len(words) -1)].strip()
    wrongGuesses = 8
    answer = "-" * len(word)
    print(hangmanStages[8 - wrongGuesses])
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
            print(hangmanStages[8 - wrongGuesses])
        else:
            answer = temp
            print("Good Guess!")

    print("\n\n")
    if answer == word:
        print("Congratulations! You won!")
    else:
        print("Unlucky, better luck next time.")
    print("The word was: " + word)
    replay = input("Would you like to play again? Enter 'y' if so, and 'n' if not: ")