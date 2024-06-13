age = int(input("enter the age:"))
name = input("enter name:")
if age >=1 and age<=10 :
    print(f"{name} with age {age} is minor")
elif age>10 and age<20 :
    print(f"{name} with age {age} is teenager")
    if age>=18:
     print(f"{name} with age {age} is legally able to vote")
else:
    print(name + " do not exist")  