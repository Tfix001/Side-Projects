import random
userInput = input("'Fair' or 'Not'? ")
a = "Rock Paper Scissors"
gameInput = (random.choice(a.split()))
if "Fair" in userInput or "fair" in userInput:
    game = True
    while game is True:
        userInput = input("Rock, Paper, or Scissors? ")
        gameInput = (random.choice(a.split()))
        print("Your input:", userInput)
        print("The computer's input:", gameInput)
        if "Rock" in userInput or "rock" in userInput:
            if "Rock" in gameInput:
                userInput = input("Tie! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
            elif "Paper" in gameInput:
                userInput = input("The computer won! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
            elif "Scissors" in gameInput:
                userInput = input("You won! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
        elif "Paper" in userInput or "paper" in userInput:
            if "Rock" in gameInput:
                userInput = input("You won! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
            elif "Paper" in gameInput:
                userInput = input("Tie! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
            elif "Scissors" in gameInput:
                userInput = input("The computer won! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
        elif "Scissors" in userInput or "scissors" in userInput:
            if "Rock" in gameInput:
                userInput = input("The computer won! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
            elif "Paper" in gameInput:
                userInput = input("You won! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
            elif "Scissors" in gameInput:
                userInput = input("Tie! Try again? ")
                if "No" in userInput or "no" in userInput:
                    game = None
                    break
        else:
            userInput = input("Error, incorrect word choice.")
elif "Not" in userInput or "not" in userInput:
    game = True
    while game is True:
        userInput = input("Rock, Paper, or Scissors? ")
        if "Rock" in userInput or "rock" in userInput:
            print("Your input:", userInput)
            print("The computer's input: Paper")
            userInput = input("The computer won! Try again? ")
            if "No" in userInput or "no" in userInput:
                game = None
                break
        elif "Paper" in userInput or "paper" in userInput:
            print("Your input:", userInput)
            print("The computer's input: Scissors")
            userInput = input("The computer won! Try again? ")
            if "No" in userInput or "no" in userInput:
                game = None
                break
        elif "Scissors" in userInput or "scissors" in userInput:
            print("Your input:", userInput)
            print("The computer's input: Rock")
            userInput = input("The computer won! Try again? ")
            if "No" in userInput or "no" in userInput:
                game = None
                break
