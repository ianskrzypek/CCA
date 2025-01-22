courselist=[]

def averagefinder(x):
    y=0
    for i in range (4):
        y=x[i][1]+y
    return round(y/4,1)
    


for i in range(4):
    while True:
        try:
            duplicatename= False
            course = input("\nEnter the name of a course you have taken this semester: ")
            for i in range(len(courselist)):
                if course in courselist[i]:
                    duplicatename=True
            if duplicatename==False:
                mark = int(input("Enter the final mark (%) you recieved in this course: "))
                if mark <= 100 and mark >= 0:
                    courselist.append([course,mark]) 
                    break
                else:
                    print("\nthe mark a student recieves cannot exceed %100 or be less than %0")
            else:
                print("\nThat subject has already be inputted")
        except:
            print("\nplease only enter a valid variable")
print("\n    Course      Mark")
average = 0
for i in range(4):
    print("   ",courselist[i][0],"   ",courselist[i][1])

average = averagefinder(courselist)

print("The average mark for these four courses is",str(average)+"%")