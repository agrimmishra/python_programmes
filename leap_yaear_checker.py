def is_leap_year(year):
    """
    Determines if the given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4.
    - However, if it is also divisible by 100, it must be divisible by 400 to be considered a leap year.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def main():
    """
    Main function to get user input and check if the year is a leap year.
    """
    try:
        # Get year input from user
        year = int(input("Enter the year: "))

        # Check if the year is a leap year
        if is_leap_year(year):
            print("Leap year")
        else:
            print("Not a leap year")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
