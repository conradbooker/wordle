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
            secretWord = secretWord.replace(guess[letter], '+', 1)
            final[letter] = guess[letter].capitalize()

    for letter in range(len(guess)):
        if guess[letter] != secretWord[letter] and guess[letter] in secretWord and secretWord[letter] != "+":
            secretWord = secretWord.replace(guess[letter], '*', 1)
            final[letter] = guess[letter].lower()
        elif guess[letter] != secretWord[letter] and guess[letter] not in secretWord and secretWord[letter] != "+" and secretWord[letter] != "*":
            final[letter] = "-"


    for char in final:
        finalStr += char

    return finalStr

print("MOTTO")
print("TOOTH")
print(getFeedback("TOOTH", "MOTTO"))

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
