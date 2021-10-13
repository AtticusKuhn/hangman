import re
from typing import Set, Tuple
def getPhrase():
    return "we love programming"
def getGameState(displayString: str, guesses:int) ->str:
    if guesses <=0:
        return "lost"
    if displayString.count("_") == 0:
        return "won"
    return "playing"
def displayInfo(displayString:str, guesses:int) ->str:
    return f'{displayString} \n\n you have {guesses} guesses left'
def isValid(guess:str) ->bool:
    return len(guess) == 1 and re.compile("[a-zA-Z]").match(guess)
def main(): #the main function defines what the program does on startup
    phrase:str = getPhrase()
    displayString = re.sub(r'[a-z]', "_", phrase)
    guessedLetters: Set[str] = set()
    guesses = 10
    while  getGameState(displayString, guesses) == "playing":
        print(displayInfo(displayString, guesses))
        userGuess = input("guess a letter> ").lower()
        if not isValid(userGuess): ## invalid guess
            print("your guess was invalid")
            continue
        elif userGuess in guessedLetters: # already guessed letter
            print("you already guessed that letter")
            continue
        elif userGuess not in phrase: #incorrect guess
            guesses -=1
            print("your guess was incorrect")
            guessedLetters.add(userGuess)
        elif userGuess in phrase: #correct guess
            print('your guess was correct')
            guessedLetters.add(userGuess)
            indicies = [n for (n, e) in enumerate(phrase) if e == userGuess]
            for i in indicies:
                temp = list(displayString)
                temp[i] = userGuess
                displayString = "".join(temp)
    if getGameState(displayString, guesses) == "lost":
        print("you lost")
    elif getGameState(displayString, guesses) == "won":
        print("you won")
if __name__ == "__main__":
    main()