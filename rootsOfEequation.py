a = int(input("enter the value of coefficient of x^2 :"))
b = int(input("enter the value of coefficient of x :"))
c = int(input("enter the value of constant :"))
checker = (b**2)-(4*(a*c))
print(checker)
if checker >0:
    print("the equation has real unequal roots :")
    x1 = ( (-1*b) - (checker**(1/2)))/(2*a)
    x2 = ( (-1*b) + (checker**(1/2)))/(2*a)
    print(x1,x2)
elif checker ==0 :
     print("the equation has real equal roots :")
     x1 = ( (-1*b) - (checker**(1/2)))/(2*a)
     print(x1)
else :
    print("equation has imaginary roots")