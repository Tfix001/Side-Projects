import random
randNum = random.randint(1, 100)
print("Guess a number between 1 & 100")
userNum = (int(input()))
while userNum is not randNum:
    if userNum < randNum:
        print("Too low")
    elif userNum > randNum:
        print("Too high")
    userNum = (int(input()))
print("Got the number!!")
