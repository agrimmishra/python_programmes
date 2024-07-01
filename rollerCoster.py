height = int(input("enter your height (in cm) :"))
if height <160:
    print("below average height not allowed")
else:
    age = int(input("enter your age :"))
    if age>5 and age<=15:
        ticketPrice = 5
    elif age>15 and age<=18:
        ticketPrice = 7
    else:
        ticketPrice = 12
        