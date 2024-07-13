import random as rand

def select_friend_for_snacks():
    """
    This function prompts the user to enter the number of friends and their names.
    It then randomly selects one of the friends to be responsible for today's snacks.
    """
    # Create a blank list to store names
    names = []

    # Taking the total number of friends for appending
    friends = int(input("Enter total number of friends: "))

    # Check if the number of friends is greater than 0
    if friends > 0:
        # Initializing the list with the names provided as input
        for i in range(friends):
            friend_name = input("Enter friend name: ")
            names.append(friend_name)
        
        # Print the list of names
        print("List of friends:", names)
        
        # Select a random index to choose a friend for snacks
        friend_index = rand.randint(0, friends - 1)
        print(f"Today's snacks are on {names[friend_index]}")
    else:
        # Handling the case where the number of friends is 0 or less
        print("You need to have at least one friend to select.")

# Call the function
select_friend_for_snacks()
