import random
userInput = input("Want to roll a dice? Type 'Yes' ")
print("How big of a dice?")
maxInt = (int(input()))
while "Yes" in userInput or "yes" in userInput:
    print(random.randint(1,maxInt))
    userInput = input("Want to roll a dice again? ")
print("Goodbye!")
