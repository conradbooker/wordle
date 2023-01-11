from wordle_wordlist import getWordList
import random

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
    possibleGuesses1 = []
    possibleGuesses2 = []

    aiGuess = "" #this AI guess will build and grow based off of the parameters
    #first, it will check in the feedbacks for uppercased letters
    #then for the lowercased, lapel --> alley, so l--El

    rand = random.randint(0,len(wordList)-1)
    if len(guesses) == 0:
        return wordList[rand]

    for guess in feedback:
        for char in range(len(guess)):
            guessChar = guess[char]
            if guessChar.islower():
                if lowerLocs.get(guessChar) == None:
                    lowerLocs[guessChar] = 0
                    lowerLocs[guessChar] += 1
                else:
                    lowerLocs[guessChar] += 1
                # guessCheck[char] =

            elif guessChar.isupper():
                capitalLocs[guessChar] = 1
                guessCheck[char] = guessChar
                print(guessCheck)
    # return capitalLocs, lowerLocs

    if capitalLocs != {}:
        for index in range(len(guessCheck)):
            # ["G", "", "", "", "T"]
            guessCheckLetter = guessCheck[index]
            print("letter: " + guessCheckLetter)

            for wordIndex in range(len(wordList)):
                word = wordList[wordIndex]

                for charIndex in range(len(word)):
                    letter = word[charIndex]

                    if guessCheckLetter == letter and charIndex == index:
                        # wordList.pop(wordIndex)
                        possibleGuesses.append(word)
        
    # return possibleGuesses
    
    for key in lowerLocs:
        for wordIndex in range(len(possibleGuesses)):
            word = possibleGuesses[wordIndex]
            if word.find(key.upper()) != -1:
                possibleGuesses2.append(word)

    return possibleGuesses


wordList = getWordList()
print(getAIGuess(wordList, ["GAUTE","EJEJE","jjjjj","aejfa"], ["G-a-T", "u-n--", "-----", "----T"]))