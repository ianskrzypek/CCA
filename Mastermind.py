import random
colors={"r":"red","b":"blue","c":"cyan","y":"yellow","o":"orange","p":"purple","w":"white","g":"grey",}
def multiplecolorcheck(x): #allows the program to know how many pairs of colors there are in your input and the answer
        hasalreadyrun = False
        doublenumber=0
        sameguess=0
        doublenumber2=0
        for i in range(4):
            for k in range(i+1,4):
                if x[i] == x[k]:
                    if hasalreadyrun == False or x[i] == doublenumber:
                        sameguess = sameguess+1
                        doublenumber = x[i]
                        hasalreadyrun = True
                    else:
                        doublenumber2 = x[i]
        if sameguess == 1:
            sameguess = 2
        elif sameguess == 6:
            sameguess = 4
        return [doublenumber,sameguess,doublenumber2]
def gameinputcheck(): #determines what answers are correct and in the right space, and correct in the wrong space
    global userguess
    global answer
    correctguess = 0
    wrongorder = 0

    userguesscheck = multiplecolorcheck(userguess) 
    answercheck = multiplecolorcheck(answer)

    if answer == userguess:
        return [4,0]
    if userguesscheck[2] != 0: #triggers in the special case that two pairs of colors are played at once
        for i in range(4):
            if userguess[i]==answer[i]:
                correctguess = correctguess+1
            elif userguesscheck[0]==answer[i]:
                if answercheck[1] > 2 and answercheck[0]==userguesscheck[0]:
                    wrongorder=2
                else:
                    wrongorder = wrongorder+1
            elif userguesscheck[2]==answer[i]:
                wrongorder = wrongorder+1
    elif userguesscheck[2]==0 and userguesscheck[1] > 0: #triggers in the event that two or more of the same color triggers at once
        for i in range(4):
            if userguess[i] == answer[i]:
                correctguess=correctguess+1
            elif userguesscheck[0] == answer[i]:
                if userguesscheck[1] <= answercheck[1]:
                    wrongorder=userguesscheck[1]
                else:
                    wrongorder= wrongorder+1
            elif userguess[i] != userguesscheck[0]:
                if userguess[i] in answer:
                    wrongorder=wrongorder+1
    else:
        for i in range(4): #triggers if no colors are the same
            if userguess[i] == answer[i]:
                correctguess = correctguess+1
            elif userguess[i] in answer:
                wrongorder = wrongorder+1
    return [correctguess,wrongorder]


while True:
    try:
        menuinput=input("""
        Mastermind
1) Play the Game
2) Exit

Enter the number of your choice: """)
        if menuinput ==("1"):
            while True:
                inputendless = input("\nDo you want to play on endless mode (Input 1, guess until you get the correct answer), \nlimited mode (Input 2, Only 12 Guesses), or hard mode (Input 3, Only 8 guesses): ")
                if inputendless == ("1"):
                    mode=1000 #sets the amount of guesses you are allowed to make
                    break
                elif inputendless==("2"):
                    mode=12
                    break
                elif inputendless==("3"):
                    mode=8
                    break
                else:
                    print("\nplease only enter the numbers 1, 2, or 3")
            answer=[]
            while True:
                inputanswerchoice=input("\nDo you want to enter your own answer to try and guess (Enter 1), or to try and guess a randomly chosen one (Enter 2)?: ")
                if inputanswerchoice == ("1"): #allows the user to choose the four colors, or let them be randomly selected
                    while len(answer) != 4:
                        print("\n",list(colors.values())) 
                        inputanswer= input("\nEnter the first letter of a color from the above list: ")
                        if inputanswer in colors:
                            answer.append(colors[inputanswer])
                        else:
                            print("\nnot a valid input")
                    break
                elif inputanswerchoice == ("2"):
                    for q in range(4):
                        answer.append(random.choice(list(colors.values()))) 
                    break
                else:
                    print("not a valid input. Please only enter the numbers 1 or 2")
            guessamount=0
            for p in range(mode): #runs the actual game
                userguess=[]
                while len(userguess) != 4:
                    print(list(colors.values()))
                    inputcolors=input("\nPlease input the first letter of a color from the above list to add it to your guess: ")
                    if inputcolors.lower in colors:
                        userguess.append(colors[inputcolors.lower()])
                        print("Input Successful")
                    else:
                        print("please only enter a the first letter of a color from the above list")
                
                guessresult=gameinputcheck()

                print("\nYour Guess was",userguess)
                guessamount=guessamount+1
                print("\nThere was",guessresult[0],"correct color(s) in the the correct space\nThere was",guessresult[1],"correct color(s) in the wrong space\nYou currently have",mode-guessamount,"guesses left")
                if guessresult[0]==4:
                    print("\nCongragulations! It took you",guessamount,"guesses to find out the code and win the game!")
                    break
                elif guessamount==mode:#checks if the amounts of turns used is the same as the amounts of turns allowed, which means the game would end
                    print("\nToo Bad! The code was:",answer)
        elif menuinput==("2"):
            print("Thank you for playing!")
            break
        else:
            print("Invalid Input. Please only enter the numbers 1 or 2")
    except:
        print("error")