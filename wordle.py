from colorama import init, Fore, Back, Style
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
            print("secretWord: " + str(secretWord))

    for letter in range(len(guess)):
        # MOMMY
        # MADAM
        if final[letter] != secretWord[letter] and final[letter] in secretWord:
            secretWord[secretWord.index(final[letter])] = "*"
            final[letter] = "*"
        print(guess[letter] + ": " + str(final))

    
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

    for char in checkedGuess:
        if char.isupper():
            colorString += (Fore.WHITE + Back.GREEN + char.upper())
        elif char.islower():
            colorString += (Fore.WHITE + Back.YELLOW + char.upper())
        else:
            colorString += (Fore.WHITE + Back.WHITE + char.upper())

    return colorString

print(getColor("TOOTH", "MOTTO"))
