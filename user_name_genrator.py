import random as ran

def usernameGen(name):
    uniqCode = str(round(ran.random()*100))
    print("user username could be : "+ name+uniqCode)
def passGen(name):
    password = str(round(ran.random()*1000))
    pas = str(password+name)
    if len (pas)>=8:
        print(pas)
    else:
        print(pas+password)

#driver code
name = input("enter name : ")
usernameGen(name)
passGen(name)