def linearSearch(list,target):
    l1 = list

    for item in l1:
        if item == target:
            return 1
        
        
l1 = [88,22,44,6,8,00,1]

if linearSearch(l1,9):    
    print("element found")
else:
    print("element not resent in list")