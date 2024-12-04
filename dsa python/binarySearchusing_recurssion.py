def binary(userlist, target, low, high):
    if low > high:
        return False

    mid = (high + low) // 2
    if userlist[mid] == target:
        return True
    elif userlist[mid] < target:
        return binary(userlist, target, mid + 1, high)
    else:
        return binary(userlist, target, low, mid - 1)

arr = [0, 1, 2, 3, 4, 5, 6]
low, high = 0, len(arr) - 1
target = 4

result = binary(arr, target, low, high)
if result:
    print("hello")
