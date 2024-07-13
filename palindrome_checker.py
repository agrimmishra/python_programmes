def isPalindrome(a):
    num = a
    sum = 0  # Variable to store the reversed number
    while num > 0:
        rem = num % 10  # Get the last digit
        sum = sum * 10 + rem  # Add it to the reversed number
        num = num // 10  # Remove the last digit from the number
    if sum == a:
        print("palindrome")  # The number is a palindrome
    else:
        print("not a palindrome")  # The number is not a palindrome

# Driver function
num = int(input("Enter a number: "))
isPalindrome(num)