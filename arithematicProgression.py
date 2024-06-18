frist_term = int(input("enter the first term of ap :"))
cD = int(input("enter the common difference  of ap :"))
noOfTerms = int(input("enter the no of terms   of ap :"))

for i in range(frist_term,frist_term+noOfTerms*cD,cD):
    print(i)