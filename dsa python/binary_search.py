list = [1,3,5,7,99,198]

def Binary(list,target):
    high = len(list)-1
    low = 0
    while low<= high:
        mid = (high + low) //2
        if target == list[mid]:
            return mid
        elif(target>list[mid]):  
            low = mid+1
        elif target<list[mid]:
            high = mid - 1
    return -1
    
index = Binary(list,99)
if index >-1:
    print(f"the element is present on {index} index ")