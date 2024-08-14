charCount = {}
string = input("enter a string :").lower()
for char in string:
    if char in charCount:
        charCount[char] +=1
    else:
        charCount[char] =1


