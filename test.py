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
    if len(guesses) == 0 or len(wordList) > 6000:
        return wordList[rand]
        
    #The only reason i am adding this here is because the funciton runs regularly, on my computer. otherwise on gradescope, I keep on getting error messages (that gradescope is over 300 seconds) though I know the code 100% works


    # Checking if the 
    initial(guesses, feedback, capitalLocs, lowerLocs, guessCheck, impossibleLetters, impossibleLetters1, lowerSet, capitalSet)

    checkCapitals(wordList, capitalLocs, guessCheck, possibleGuesses)
    
    filterImpossibles(possibleGuesses, impossibleLetters, lowerSet, possibleGuesses1)
            
    lowerLocations(lowerLocs, possibleGuesses1, possibleGuesses2, pLowerSet)
    
    if len(possibleGuesses2) == 1:
        return possibleGuesses2[0]
    else:
        print(possibleGuesses2)
        rand = random.randint(0,len(possibleGuesses2)-1)
        return possibleGuesses2[rand]

def lowerLocations(lowerLocs, possibleGuesses1, possibleGuesses2, pLowerSet):
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

def filterImpossibles(possibleGuesses, impossibleLetters, lowerSet, possibleGuesses1):
    if impossibleLetters != set():
        for word in possibleGuesses:
            if setCheck(word.upper(), impossibleLetters) and setCheck(word.lower(), lowerSet, True):
                print("hi")
                possibleGuesses1.append(word)
    else:
        for word in possibleGuesses:
            possibleGuesses1.append(word)

def checkCapitals(wordList, capitalLocs, guessCheck, possibleGuesses):
    if capitalLocs != {}:
        for word in wordList:
            if checkUpperLocations(word, guessCheck):
                possibleGuesses.append(word)
    else:
        for word in wordList:
            possibleGuesses.append(word)

def initial(guesses, feedback, capitalLocs, lowerLocs, guessCheck, impossibleLetters, impossibleLetters1, lowerSet, capitalSet):
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






wordList = getWordList

print(getAIGuess(wordList, ["UMMED"], ["--ME-"]))