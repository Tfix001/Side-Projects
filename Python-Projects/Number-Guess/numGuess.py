import random
lowNum = (int(input("Input a low range number: ")))
highNum = (int(input("Input a high range number: ")))
randNum = random.randint(lowNum, highNum)
print("Guess a number between", int(lowNum), '&', int(highNum))
userNum = (int(input()))
while userNum is not randNum:
    if userNum < randNum:
        print("Too low")
    elif userNum > randNum:
        print("Too high")
    userNum = (int(input()))
print("Got the number!!")
