def linearSearch(list,target):
    for item in list:
        if item == target:
            return 1
        else:
            return 0;
        
list = [22,33,44,67,88,00]
result = linearSearch(list,9)
if result == 1:
    print("element found");
else:
    print("element not found")