devicecost = {"iPad":500,"Macbook":1300,"iPhone":1130,"Samsung":1100}
def calcTax(x):
    return round(x*.13,2)

while True:
    device = input("""\n    *** Sales Tax Calculator ***
List of Items:
1) iPad
2) Macbook
3) iPhone
4) Samsung
Enter the name of number of an item from the above list: 
""")
    if device.lower() == "ipad" or device == "1":
        print("You have selected the Ipad")
        device ="iPad"
        break
    elif device.lower() == "macbook" or device == "2":
        print("You have selected the Macbook")
        device="Macbook"
        break
    elif device.lower() == "iphone" or device == "3":
        print("You have selected the iPhone")
        device = "iPhone"
        break
    elif device.lower() == "samsung" or device == "4":
        print("You have selected the Samsung")
        device = "Samsung"
        break
    else:
        print("Please only enter the name or number of an item showed in the above list")
cost = devicecost[device]
print("\nThe price of this item is:\n",cost)
while True:
    StudentPriceCard = input("\nDo you have a Student Price Card? (enter yes or no):\n")
    if StudentPriceCard.lower() == "yes" or StudentPriceCard.lower() == "y":
        print("You will now reviece a 15% price reduction")
        StudentPriceCard = True
        break
    elif StudentPriceCard.lower() == "no" or StudentPriceCard.lower() == "n":
        print("You will not recieve any price reductions")
        StudentPriceCard = False
        break
    else:
        print("Please only enter 'yes' or 'no'")

print("\n   ",device,"   $"+str(cost))
if StudentPriceCard == True:
    cost = round(cost*.85,2)
    print("    Reduced Student Price   $"+str(cost))
tax = round(calcTax(cost),2)
print("    Sales Tax    $"+str(tax),"\n    Total Cost    $"+str(cost+tax))
