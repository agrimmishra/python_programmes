def snackOrder():
    snacks = input("Enter the snack you want to buy: ").lower()
    if snacks == "burger":
        sncId = 1001
        return sncId
    elif snacks == "pizza":
        sncId = 1002
        return sncId
    elif snacks == "hotdog": 
        sncId = 1003
        return sncId
    else:
        print("Sorry, we don't have that snack.")

def drinkOrder():
    drink = input("Enter the drink you want to buy: ").lower()
    if drink == "coke":
        drkId = 10001
        return drkId
    elif drink == "shake":
        drkId = 10002
        return drkId
    else:
        print("Sorry, we don't have that drink.")

# Driver function
snID = snackOrder()
drID = drinkOrder()

if snID and drID:  # Check if both snack and drink IDs are valid
    if snID == 1001 and drID == 10001:
        price = 100
    elif snID == 1001 and drID == 10002:
        flv = input("Enter flavor of the shake (banana/strawberry): ").lower()
        if flv == "banana":
            price = 110
        elif flv == "strawberry":
            price = 115

    elif snID == 1002 and drID == 10001:
        price = 150
    elif snID == 1002 and drID == 10002:
        flv = input("Enter flavor of the shake (banana/strawberry): ").lower()
        if flv == "banana":
            price = 160
        elif flv == "strawberry":
            price = 155

    elif snID == 1003 and drID == 10001:
        price = 160
    elif snID == 1003 and drID == 10002:
        flv = input("Enter flavor of the shake (banana/strawberry): ").lower()
        if flv == "banana":
            price = 170
        elif flv == "strawberry":
            price = 165

    else:
        print("Invalid combination of snack and drink.")

    if 'price' in locals():
        bill = price + (price * 0.15)  # Adding 15% tax
        print(f"Total bill: ${bill:.2f}")

