def  factFinder(num):
    if num == 1 or num ==0:
        num =1
        return num
    else:
        num = num*factFinder(num-1)
        return num
    

print(factFinder(45))
