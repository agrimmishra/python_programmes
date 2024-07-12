def Selfdivide(num):
    """
    Checks if a number is a self-dividing number.
    
    Parameters:
    num (str): The number to check, represented as a string.
    
    Returns:
    bool: True if the number is self-dividing, False otherwise.
    """
    num1 = int(num)  # Convert the input string to an integer
    for digit in num:
        digit = int(digit)  # Convert each character to an integer
        if digit == 0 or num1 % digit != 0:  # Check if the digit is 0 or if num1 is not divisible by the digit
            return False  # If either condition is true, the number is not self-dividing
    return True  # If all digits pass the checks, the number is self-dividing

# Prompt the user to enter a number
num = input("Enter number: ")

# Check if the entered number is self-dividing and print the result
if Selfdivide(num):
    print(f"{num} is a self-dividing number")
else:
    print(f"{num} is not a self-dividing number")
