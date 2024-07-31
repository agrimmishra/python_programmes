def sumNum(givenNum):
    """
    Computes the digital root of a given number.

    The digital root is the iterative process of summing the digits of a number until a single digit is obtained.

    Parameters:
    givenNum (int): The number whose digital root is to be calculated.

    Returns:
    int: The digital root of the given number.
    """
    # Initialize a variable to store the sum of digits
    number = givenNum
    sum = 0

    # Calculate the sum of digits of the number
    while number > 0:
        rem = number % 10  # Get the last digit
        sum += rem         # Add it to the sum
        number //= 10      # Remove the last digit

    # If the sum is a single digit, return it
    if sum < 10:
        return sum
    else:
        # Recursively call sumNum to reduce the sum to a single digit
        return sumNum(sum)

# Input number from the user
num = int(input("Enter number: "))

# Calculate and print the digital root of the input number
result = sumNum(num)
print("The digital root is:", result)
