import csv

othercharacters = ["!","$","%","&","<",">","*","@","£","(",")","#","~"]
def enterpassword(x=1): #function used to help enter the password both when making the id, and when changing the password of an existing id
    global password
    while True:
        password = input("\nPlease enter a password to link to your user ID. This password will be ranked on length, if it contains uppercase and lowercase letters, \nif it contains special characters (ex. !,@), and if it contains numbers: ")
        passwordcheck()
        print (passwordpoints)
        if passwordpoints < 3:
            print("\nYour password is weak, and only gained",passwordpoints,"points out of 5. Please come up with a better one")
        elif passwordpoints < 5:
            if x ==1: #triggers when making a new id, becuause a 3 or 4 out of 5 is somewhat acceptable
                print("\nYour password could be improved. It gained",passwordpoints,"points out of 5. Enter '1' to exit, or '2' to be able to remake your password.")
                exitinput = input("Please note that your user ID will only be added to the file 'IDs.csv' if it recieves a 5/5: ")
                if exitinput == ("1"):
                    break
            elif x==2: #triggers when changing an existing password, becuase only a 5/5 will be acceptable for the IDs.csv file
                print("\nYour password could be improved. It gained",passwordpoints,"points out of 5")
        elif passwordpoints == 5:
            print("\nNice job! You recieved a 5 out of 5 for your password. It will be stored in the file 'IDs.csv'")
            break
    return
def passwordcheck(): #Function used to check which of the requirements the password meats
    global password
    global passwordpoints
    othercharacters = ["!","$","%","&","<",">","*","@","£"]
    passwordpoints=0
    if len(password) > 7:
        passwordpoints=passwordpoints+1
    for i in range(len(password)):
        if 64 < ord(password[i]) and ord(password[i]) < 91:
            passwordpoints=passwordpoints + 1
            break
    for i in range(len(password)):
        if 96 < ord(password[i]) and ord(password[i]) < 123:
            passwordpoints = passwordpoints+1
            break
    for i in range(len(password)):
        if 47 < ord(password[i]) and ord(password[i]) < 58:
            passwordpoints = passwordpoints + 1
            break
    for i in range(len(password)):
        if password[i] in othercharacters:
            passwordpoints = passwordpoints+1
            break
    return
def makeID(): #helps in the making of a user id
    global password
    global userid
    while True:
        userid = input("\nEnter a new user ID: ")
        ids = open("IDs.csv","r")
        if userid in ids.read():
            print("\nThat ID is already in use. Please select another one")
        else:
            break
    ids.close()
    enterpassword()
    if passwordpoints == 5:
        IDs = open("IDs.csv","a")
        IDs.write("\n"+userid+", "+password)
        IDs.close()
    return
def passwordchange(): #
        end=1
        global password
        ids = list(csv.reader(open("IDs.csv")))  #reads original csv
        idslist = [] 
        for row in ids:
            idslist.append(row)
        fileidcheck = input("Enter a user's ID to change their password: ")
        for i in range(1,len(idslist)):
            if fileidcheck in idslist[i]:
                enterpassword(2)
                idslist[i][1]=password
                end =2
                break
        if end ==1:
            print("ID not found")
            return            
        ids = open("IDs.csv","w")
        for i in range (1,len(idslist)):
            ids.write("\n"+idslist[i][0]+", "+idslist[i][1])
        ids.close()
        return         

ids = open("IDs.csv","a") #making sure a ids.csv file actually exists so errors dont pop up
ids.close()

while True:
    try:
        menuinput = input("""
1) Create a new user ID
2) Change a password
3) Display all User ID's
4) Exit
                          
Enter selection: """)
        if menuinput==("1"):
            makeID()
        elif menuinput==("2"):
            passwordchange()
        elif menuinput==("3"):
            idslist=[]
            ids = list(csv.reader(open("IDs.csv"))) #Reads the IDs file and prints the user ids
            for i in range(1,len(ids)):
                idslist.append(ids[i][0])
            print("\n",idslist)
        elif menuinput==("4"):
            print("Thank you for trying my ID writer!")    
            break
        else:
            print("invalid input")
    except:
        print("Error")