def shiftcode(x=2): #shifts the code left and right
    newmessage=("")
    message = input("\nenter the message you want to shift (only capital and lowercase letters will be changed, but any character may be inputted): ")
    while True:
        try:
            shiftlength = int(input("\nEnter the amount you want to shift your message by (will be shifted right if you selected 1, and left if you selected 2 in the menu): "))
            if x == 1:
                shiftlength = -shiftlength #switches the shift amount to negative to allow it to go the left
            break
        except:
            print("Your input must be a number")
    for i in range(len(message)):
        tempstorage = ord(message[i])
        if tempstorage < 91 and tempstorage > 64: #allows capitals to stay capital, and lowercase letters to stay lowercase
            tempstorage = (tempstorage+shiftlength-65)%26+65
            newmessage=newmessage+chr(tempstorage)
        elif tempstorage < 123 and tempstorage > 96:
            tempstorage = (tempstorage+shiftlength-97)%26+97
            newmessage=newmessage+chr(tempstorage)
        else:
            newmessage = newmessage+chr(tempstorage)
    print("\n"+newmessage)

while True:
    #try:
        inputmenu = input("""
1) Make a Code
2) Decode a Message
3) Exit
                          
Make your Selection: """)
        if inputmenu=="1":
            shiftcode()
        elif inputmenu=="2":
            shiftcode(1)
        elif inputmenu=="3":
            print("\nThank you for trying my code shifter")
            break
    #except:
        #print("Error")