import random as random
genNum =random.randint(0,100)
for i in range(5,0,-1):
    num = int(input("enter number :"))
    if i>1:
        if num > genNum:
            print("try guessing a smaller number")
        elif num <genNum:
            print("try guessing a bigger number")
        elif num == genNum:
            print("hurray! you gussed the number")
            break
    else:
        print("no changes left\nthe number you were guessing was ", genNum)

