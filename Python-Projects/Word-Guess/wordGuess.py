import random
wordList = "Awkward Bagpipes Crypt Dwarves Endlong Fervid Gazebo Haphazard Ivory Jinx Klutz Leech Mystify Numbskull Oxygen Phlegm Quip Rhythmic Swivel Twelfth Unwithdrawing Vair Wheeple Xenophobia Yelt Zeugmatography"
wordBase = random.choice(wordList.split())
word = list(wordBase)
givenWord = list('*'*len(word))
game = True
userGuess = input("Would you like to play hangman? ")
if "Yes" in userGuess or "yes" in userGuess:
    while game is True:
        print(givenWord)
        userGuess = input("Guess a letter (Case sensitive) ")
        for i in range(0,len(word)):
            if userGuess in word[i]:
                givenWord[i] = userGuess
        for i in range(0, len(word)):
            if givenWord[i] not in word[i]:
                game = True
                break
            else:
                game = None
        if game is None:
            print("You win!! The word was", wordBase)

else:
    print("Oh, well, goodbye in that case!")
