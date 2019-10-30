print("Pick a range of numbers X - Y")
lowNum = (int(input("Low Number: ")))
highNum = (int(input("High Number: ")))
mid = (lowNum + highNum) / 2
userInput = "No"
while userInput is not "Yes"
    print("Is ", mid, " the number?")
    userInput = input()
    if userInput is not "Yes"
        userInput = input("Higher or Lower?")
        if userInput is "Higher"
            mid = (mid + highNum) / 2
            if mid is highNum
                print("Is ", highNum, " the number?")
                userInput = input()
                    if userInput is not "Yes"
                        print("Number is not in range")
                        break
        else
            mid = (lowNum + mid) / 2
            if mid is lowNum
                print("Is ", lowNum, " the number?")
                userInput = input()
                    if userInput is not "Yes"
                        print("Number is not in range")
                        break
if userInput is "Yes"
    print("Got the number! It was ", mid)
else
    print("Sorry, I couldn't guess it")
