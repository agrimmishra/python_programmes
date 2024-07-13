count = int(input("enter the counter : "))
counter = 0
nsum =0
psum=0
while(counter<count):
    nums = int(input("enter no :"))
    if nums > 0:
        psum = psum+nums
    else:
        nsum = nsum+nums
    counter+=1
print(psum,"is the sum of all positive numbers you entered")
print(nsum,"is the sum of all negetive numbers you entered")