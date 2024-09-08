def converdec(decnum):
    binum = 0
    pow = 1
    while(decnum>0):
        rem = decnum%2
        decnum = decnum//2
        binum += rem*pow
        pow *= 10
    return binum

print(converdec(4))
