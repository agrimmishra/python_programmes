def snackOrder():
    # Prompt the user to enter the snack they want to buy
    snacks = input("Enter the snack you want to buy: ").lower()
    # Check for available snacks and return the corresponding snack ID
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
        # Inform the user if the snack is not available
        print("Sorry, we don't have that snack.")

def drinkOrder():
    # Prompt the user to enter the drink they want to buy
    drink = input("Enter the drink you want to buy: ").lower()
    # Check for available drinks and return the corresponding drink ID
    if drink == "coke":
        drkId = 10001
        return drkId
    elif drink == "shake":
        drkId = 10002
        return drkId
    else:
        # Inform the user if the drink is not available
        print("Sorry, we don't have that drink.")

# Driver function to take snack and drink orders
snID = snackOrder()
drID = drinkOrder()

# Check if both snack and drink IDs are valid
if snID and drID:
    # Determine the price based on the combination of snack and drink
    if snID == 1001 and drID == 10001:
        price = 100
    elif snID == 1001 and drID == 10002:
        # Prompt for shake flavor if shake is ordered
        flv = input("Enter flavor of the shake (banana/strawberry): ").lower()
        if flv == "banana":
            price = 110
        elif flv == "strawberry":
            price = 115

    elif snID == 1002 and drID == 10001:
        price = 150
    elif snID == 1002 and drID == 10002:
        # Prompt for shake flavor if shake is ordered
        flv = input("Enter flavor of the shake (banana/strawberry): ").lower()
        if flv == "banana":
            price = 160
        elif flv == "strawberry":
            price = 155

    elif snID == 1003 and drID == 10001:
        price = 160
    elif snID == 1003 and drID == 10002:
        # Prompt for shake flavor if shake is ordered
        flv = input("Enter flavor of the shake (banana/strawberry): ").lower()
        if flv == "banana":
            price = 170
        elif flv == "strawberry":
            price = 165

    else:
        # Inform the user if the combination is invalid
        print("Invalid combination of snack and drink.")

    # Check if the price is set and calculate the total bill with tax
    if 'price' in locals():
        bill = price + (price * 0.15)  # Adding 15% tax
        print(f"Total bill: ${bill:.2f}")
