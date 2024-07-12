def VnCcounter(str):
    """
    Count the number of vowels and consonants in a given string.

    Parameters:
    str (str): The input string to count vowels and consonants from.

    Returns:
    None. Prints the counts of vowels and consonants in the string.

    Example:
    >>> VnCcounter("hello world")
    3 vowels and 7 consonants
    """
    v_count = 0
    c_count = 0
    vowels = ["a", "e", "i", "o", "u"]

    # Check if the string is empty or contains only spaces
    if str.strip() == "":
        print("String is empty or contains only spaces.")
        return

    for ch in str.lower():  # Convert to lowercase to handle case insensitivity
        if ch.isalpha():  # Check if the character is an alphabet
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
        # Ignore non-alphabet characters (numbers, symbols, spaces, etc.)

    print(f"{v_count} vowels and {c_count} consonants")

#Driver Function
name = input("Enter your name: ")
VnCcounter(name)
