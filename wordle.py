from colorama import init, Fore, Back, Style
from wordle_wordlist import getWordList
import random
init()
import itertools



def getFeedback(guess, secretWord):
    '''Generates a feedback string based on comparing guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter
        - Correct letter, wrong spot: lowercase letter
        - Letter not in the word: '-'

       For example:
        - getFeedback("lever", "EATEN") --> "-e-E-"
        - getFeedback("LEVER", "LOWER") --> "L--ER"
        - getFeedback("MOMMY", "MADAM") --> "M-m--"
        - getFeedback("ARGUE", "MOTTO") --> "-----"

        Args:
            guess (str): The guessed word
            secretWord (str): The secret word
        Returns:
            str: Feedback string, based on comparing guess with the secret word
    '''

    guess = guess.lower()
    secretWord = secretWord.lower()
    secretWord = list(secretWord)
    final = list(guess)
    finalStr = ""

    if guess == secretWord:
        return secretWord.upper()

    # ("MOMMY", "MADAM") --> "M-m--"

    # round 1: find the equals
    # round 2: find the locations
    # round 3: find the nonequals

    # + is found
    # letter is not found


    for letter in range(len(guess)):
        if guess[letter] == secretWord[letter]:
            secretWord[letter] = "+"
            final[letter] = "+"
            # print("secretWord: " + str(secretWord))

    for letter in range(len(guess)):
        # MOMMY
        # MADAM
        if final[letter] != secretWord[letter] and final[letter] in secretWord:
            secretWord[secretWord.index(final[letter])] = "*"
            final[letter] = "*"
        # print(guess[letter] + ": " + str(final))

    
    for char in range(len(final)):
        if final[char] == "+":
            finalStr += guess[char].upper()
        elif final[char] == "*":
            finalStr += guess[char]
        else:
            finalStr += "-"

    return finalStr

print("MOTTO")
print("TOOTH")
print(getFeedback("TOOTH", "MOTTO"))
print("1", "1".isalpha())

def getColor(guess, secretWord):
    checkedGuess = getFeedback(guess, secretWord)
    colorString = ""

    for i in range(len(checkedGuess)):
        if checkedGuess[i].isupper():
            colorString += (Fore.WHITE + Back.GREEN + guess[i].upper())
            colorString += (Style.RESET_ALL)
        elif checkedGuess[i].islower():
            colorString += (Fore.WHITE + Back.YELLOW + guess[i].upper())
            colorString += (Style.RESET_ALL)
        else:
            colorString += (Style.RESET_ALL)
            colorString += (Fore.WHITE + guess[i].upper())
            colorString += (Style.RESET_ALL)

    return colorString

print(getColor("TOOTH", "MOTTO"))

def playGame(wordList):
    secretWord = wordList[random.randint(0, len(wordList))]
    print(F"\n-----Welcome to WORDLE-----\n")
    guess = input("Enter 5 letter guess (\"AI\") for AI: ")
    guesses = []
    feedbacks = []

    if guess.lower() == "ai":
        guess = getAIGuess(wordList, guesses, feedbacks)
    else:
        while guess.upper() not in wordList:
            guess = input("Input a valid word: ")

    feedback = getColor(guess, secretWord)
    print(feedback)
    attempts = 1
    guesses.append(guess)

    while attempts <= 5 and guess.lower() != secretWord.lower():
        guess = input("Enter guess (\"AI\") for AI: ")
        attempts += 1

        if guess.lower() == "ai":
            guess = getAIGuess(wordList, guesses, feedbacks)
        else:
            while guess.upper() not in wordList:
                guess = input("Input a valid word: ")
        guesses.append(guess)
        feedbacks.append(getFeedback(guess, secretWord))
        # top and bottom border here
        feedback = ""
        feedback += (getColor("whitespace at the top"))
        for guessNew in guesses:
            feedback += "\n" + getColor(guess, secretWord)
        feedback += (getColor("whitespace at the bottom"))
        print(feedback)

    if secretWord == guess:
        print("You win!")
    else:
        print("You lost!")
        print("The secret word was: " + secretWord)

def getAIGuess(wordList, guesses, feedback):
    '''Analyzes feedback from previous guesses (if any) to make a new guess
        Args:
            wordList (list): A list of potential Wordle words
            guesses (list): A list of string guesses
            feedback (list): A list of feedback strings
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''

    capitalLocs = {}
    lowerLocs = {}

    rand = random.randint(0,len(wordList)-1)
    if len(guesses) == 0:
        return wordList[rand]

    for guess in feedback:
        for char in guess:
            if char.Islower():
                if lowerLocs.get(char) == None:
                    lowerLocs[char] = 0
                else:
                    lowerLocs[char] += 1
            elif char.isupper():
                if capitalLocs.get(char) == None:
                    capitalLocs[char] = 0
                else:
                    capitalLocs[char] += 1




    # ["-e-E-",""]



wordList = getWordList()
playGameBool = True

while playGameBool == True:
    playGame(wordList)
    playAgain = input("Do you want to play again?")
    if playAgain.lower() not in ["yes","y","yas","yass","uh huh"]:
        playGameBool = False
    
    