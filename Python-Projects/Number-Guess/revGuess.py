print("Pick a range of numbers X - Y")
lowNum = (int(input("Low Number: ")))
highNum = (int(input("High Number: ")))
mid = int((lowNum + highNum) / 2)
low1 = lowNum
high1 = highNum
userInput = "No"
while "Yes" not in userInput:
    print("Is", mid, "the number?")
    userInput = input()
    if "Yes" not in userInput:
        userInput = input("Higher or Lower? ")
        if "Higher" in userInput:
            low1 = int(mid)
            mid = int((mid + high1) / 2)
            if mid is low1:
                print("Is", high1, "the number?")
                userInput = input()
                if "No" in userInput:
                    print("Number is not in the range", lowNum, "-", highNum)
                    break
        elif "Lower" in userInput:
            high1 = int(mid)
            mid = int((low1 + mid) / 2)
            if mid is high1:
                print("Is", low1, "the number?")
                userInput = input()
                if "No" in userInput:
                    print("Number is not in the range", lowNum, "-", highNum)
                    break
if "Yes" in userInput:
    print("Got the number! It was", mid)
else:
    print("Sorry, I couldn't guess it")
