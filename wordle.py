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


def getColor(guess, secretWord):
    checkedGuess = getFeedback(guess, secretWord)
    colorString = (Back.WHITE + " ")

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

    colorString += (Back.WHITE + " ")
    colorString += (Style.RESET_ALL)

    return colorString

def playGame(wordList):
    secretWord = "BROOM"
    print(F"\n-----Welcome to WORDLE-----\n")
    guess = input("Enter 5 letter guess ('AI') for AI:\n")
    guesses = []
    feedbacks = []

    if guess.lower() == "ai":
        guess = getAIGuess(wordList, guesses, feedbacks)
    else:
        while guess.upper() not in wordList:
            guess = input("Input a valid word:\n")

    feedback = (Style.RESET_ALL+ Back.WHITE + "       \n" + getColor(guess, secretWord) + "       \n" + Style.RESET_ALL)
    print(feedback)
    attempts = 1
    guesses.append(guess.upper())
    feedbacks.append(getFeedback(guess, secretWord))

    while attempts <= 5 and guess.lower() != secretWord.lower():
        guess = input("Enter guess ('AI') for AI:\n")
        attempts += 1

        if guess.lower() == "ai":
            guess = getAIGuess(wordList, guesses, feedbacks)
        else:
            while guess.upper() not in wordList:
                guess = input("Input a valid word:\n")
        guesses.append(guess.upper())
        feedbacks.append(getFeedback(guess, secretWord))
        # top and bottom border here
        feedback += ("\n" + getColor(guess, secretWord))
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
    guessCheck = ["","","","",""]
    possibleGuesses = []
    impossibleLetters = set()
    impossibleLetters1 = set()
    lowerSet = set()
    capitalSet = set()

    possibleGuesses1 = []
    possibleGuesses2 = []

    pLowerSet = []

    for guess in guesses:
        guess = guess.upper()

    rand = random.randint(0,len(wordList)-1)
    if len(guesses) == 0:
        return wordList[rand]
        
    #Initial
    for feedbackIndex in range(len(feedback)):
        guess = feedback[feedbackIndex]
        for char in range(len(guess)):
            guessChar = guess[char]
            if guessChar.islower():
                if lowerLocs.get(guessChar) == None:
                    lowerLocs[guessChar] = set()
                    lowerLocs[guessChar].add(char)
                else:
                    lowerLocs[guessChar].add(char)
                lowerSet.add(guessChar)

            elif guessChar.isupper():
                capitalLocs[guessChar] = 1
                capitalSet.add(guessChar)
                guessCheck[char] = guessChar
            
            else: # if the character is a "-"
                impossibleLetters1.add(guesses[feedbackIndex][char])

    for char in impossibleLetters1:
        if char.lower() not in lowerSet and char.upper() not in capitalSet:
            impossibleLetters.add(char)

    
    if capitalLocs != {}:
        for word in wordList:
            if checkUpperLocations(word, guessCheck):
                possibleGuesses.append(word)
    else:
        for word in wordList:
            possibleGuesses.append(word)
    
    # if len(wordList) > 10000:
    #     rand = random.randint(0,len(possibleGuesses)-1)
    #     return possibleGuesses[rand]
 

    if len(possibleGuesses) == 1:
        return possibleGuesses[0]

    if impossibleLetters != set():
        for word in possibleGuesses:
            if setCheck(word.upper(), impossibleLetters) and setCheck(word.lower(), lowerSet, True):
                possibleGuesses1.append(word)
    else:
        for word in possibleGuesses:
            possibleGuesses1.append(word)

    if len(possibleGuesses1) == 1:
        return possibleGuesses1[0]


    if lowerLocs != {}:
        # Each word
        for index in range(len(possibleGuesses1)):
            word = possibleGuesses1[index]

            for key in lowerLocs:
                if word.find(key) not in lowerLocs[key]:
                    pLowerSet.append(True)
                else:
                    pLowerSet.append(False)
            
            if all(pLowerSet):
                possibleGuesses2.append(word)
            pLowerSet = []

            # if lowerCheck(lowerLocs)
    else:
        for index in possibleGuesses1:
            possibleGuesses2.append(index)
        
    if len(possibleGuesses2) == 1:
        return possibleGuesses2[0]
    else:
        # print(possibleGuesses2)
        rand = random.randint(0,len(possibleGuesses2)-1)
        return possibleGuesses2[rand]


def setCheck(word, set, containsAll = False):
    if containsAll:
        for char in set:
            if char not in word: return False
        return True
    else:
        for char in set:
            if char in word: return False
        return True

def checkUpperLocations(word, guessCheck):
    '''Checks locations
        Args:
            word (string): A word
            guessesCheck (list): A list of string things
        Returns:
         boolean, true if there are all the guesscheck locations in the word, and a false if there are not
    '''
    temp = []
    guessCheckNum = 0

    for char in guessCheck:
        if char.isalpha():
            guessCheckNum += 1

    for index in range(len(word)):
        letter = word[index]
        isChecked = False
        for guessIndex in range(len(guessCheck)):
            guessLetter = guessCheck[guessIndex]
            if letter == guessLetter and guessIndex == index:
                isChecked = True
                break
            else:
                isChecked = False
        if isChecked:
            temp.append(letter)
        else:
            temp.append("")
    
    if guessCheck == temp:
        return True
    return False


wordList = getWordList()

playGameBool = True

while playGameBool == True:
    playGame(wordList)
    playAgain = input("Do you want to play again?\n")
    if playAgain.lower() not in ["yes","y","yas","yass","uh huh"]:
        playGameBool = False
    
    