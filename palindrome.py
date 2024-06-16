def isPlaindrome(a):
    num = a
    sum =0
    while num >0:
        rem = num%10
        sum = sum*10+rem
        num = num //10
    if sum == a:
        print("palindrome")
    else:
        print("not a palindrome")
        
#driver function
num = int(input("enter a number "))
isPlaindrome(num)