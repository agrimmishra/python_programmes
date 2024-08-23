def factCalc(number):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    number (int): The number to calculate the factorial of. 
    Must be a non-negative integer.

    Returns:
    int: The factorial of the given number.
    
    Example:
    >>> factCalc(5)
    120
    """
    if number == 0 or number == 1:
        return 1
    else:
        return number * factCalc(number - 1)

# User input with a clear message
n = int(input("Enter the total number of items (n): "))
r = int(input("Enter the number of items to choose (r): "))

# Calculate nCr and print the result
ncr = factCalc(n) // (factCalc(r) * factCalc(n - r))
print(f"The number of ways to choose {r} items from {n} items is: {ncr}")
