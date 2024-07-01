photoPrice = 3
name  = input("enter your name :")
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
    photo = input("do you want a photo :")
    
    if photo.lower() == "y":
        bill = ticketPrice + photoPrice
        print(f"bill details\n your name is : {name}\n your ticket price is : ${ticketPrice}\n photo charge : ${photoPrice}\n your final bill is : ${bill}")
    else:
      bill= ticketPrice
    print(f"bill details\n your name is : {name}\n your ticket price is : ${ticketPrice}\n your final bill is : ${bill}")