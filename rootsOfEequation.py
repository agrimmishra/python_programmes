a = int(input("enter the value of coefficient of x^2 :"))                                       #  taking in the co-efficient of the eqution      
b = int(input("enter the value of coefficient of x :"))
c = int(input("enter the value of constant :"))
checker = (b**2)-(4*(a*c))                                                                                #  checking the behavoir of the roots of equation
print("the Discrimant for the equation " , checker)
if checker >0:                                                                                                   # conditon for unequal roots 
    print("the equation has real unequal roots :")
    x1 = ( (-1*b) - (checker**(1/2)))/(2*a)
    x2 = ( (-1*b) + (checker**(1/2)))/(2*a)
    print(x1,x2)
elif checker ==0 :                                                                                          # condition for equal roots 
     print("the equation has real equal roots :")
     x1 = ( (-1*b) - (checker**(1/2)))/(2*a)
     print(x1)
else :
    print("equation has imaginary roots")