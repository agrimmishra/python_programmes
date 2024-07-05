import random as rand

names = [] # create a blank list 
friends = int(input("enter total no of friends : ")) #taking the the total number of friends for appending
for i in range (0,friends):
    friendNm = input("enter friend name :")  #intialising the list with the names so input
    names.append(friendNm)
print(names) #printing the list of names 
frIndx = rand.randint(0,friends-1)
print(f"today's sancks are on {names[frIndx]}")