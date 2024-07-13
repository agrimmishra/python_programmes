num = int(input("enter the number"))

for i in range (1,num+1):
    count = 0
    for j in range (1,num+1):
        if i%j == 0:
            count+=1
    if count == 2:
        print(i)