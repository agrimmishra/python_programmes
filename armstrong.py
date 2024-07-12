def ArmstrongChecker(num):
    """
    Check if a given number is an Armstrong number.

    An Armstrong number (also known as a narcissistic number) is a number that 
    is equal to the sum of its own digits each raised to the power of the 
    number of digits.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is an Armstrong number, False otherwise.

    Example:
    >>> ArmstrongChecker(153)
    True
    >>> ArmstrongChecker(123)
    False
    """
    # Convert the number to a string to determine its length
    num_str = str(num)
    
    # Initialize temporary variable and sum
    temp = num
    sum = 0
    
    # Loop to extract each digit and calculate the sum of the digits raised to the power of the number's length
    while temp > 0:
        rem = temp % 10  # Get the last digit
        sum += rem ** len(num_str)  # Add the digit raised to the power of the length of the number
        temp //= 10  # Remove the last digit
    
    # Check if the sum is equal to the original number
    return sum == num

# Driver code
number = int(input("Enter the number: "))
if ArmstrongChecker(number):
    print(f"Entered value {number} is an Armstrong number")
else:
    print(f"Entered value {number} is not an Armstrong number")
