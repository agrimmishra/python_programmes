def sumNum(givenNum):
    number = givenNum
    sum=0
    while number>0:
        rem = number%10
        sum+=rem
        number//=10
        newNum= sum
  
    if(newNum>10):
       sumNum(newNum)
    else:
       print(newNum)
    
    
num = int(input("enter number:"))
sumNum(num)
          
          