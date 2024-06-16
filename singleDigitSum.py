def sumNum(a):
    number = a
    sum=0
    while number>0:
        rem = number%10
        sum+=rem
        number//=10
    new = sum
    if(new>10):
        sumNum(new)
    else:
     print(new)
    
    
num = int(input("enter number:"))
sumNum(num)
          
          