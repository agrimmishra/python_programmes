noOfTerm = int(input("enter no of terms :"))
a = 0
b =1
for i in range (noOfTerm):
    print(a,end=" ")
    c = a+b
    a=b
    b=c
    