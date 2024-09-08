list= []
num = int(input("enter the number"))
for n in range(2,num):
    for i in range(2,num):
        if n%i ==0:
            num+=1
        else:
            list.append(n)
print(list)