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
    final = ""
    breaking = False

    # ("MOMMY", "MADAM") --> "M-m--"

    # round 1: find the equals
    # round 2: find the locations
    # round 3: find the nonequals

    for letter in range(len(guess)):
        if guess[letter] == secretWord[letter]:
            secretWord = secretWord.replace(guess[letter], '+', 1)
            final += guess[letter].capitalize()

        elif guess[letter] != secretWord[letter] and guess[letter] in secretWord:
            
            if secretWord.count(guess[letter]) == 1:
                for char in range(len(guess)):
                    if guess[char] == secretWord[char]:
                        breaking = True
                        break
            
            if breaking == False:
                secretWord = secretWord.replace(guess[letter], '+', 1)
                final += guess[letter].lower()
            
            else:
                final += "-"

        else:
            final += "-"

    return final

print("MOTTO")
print("TOOTH")
print(getFeedback("TOOTH", "MOTTO"))
