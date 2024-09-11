def isprime(num):
    if num<2:
        return False;
    else :
        for i in range(2,int(num**(0.5))+1):
            if num%i == 0:
                return False
    return True

def printprimes(start , end):
    primes =[]
    for i in range (start,end):
        if isprime(i):
            primes.append(i)
    return primes
start = int(input("enter the starting number :"))
end = int(input("enter the ending number :"))
print(printprimes(start,end))
    
