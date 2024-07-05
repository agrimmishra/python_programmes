boyNm = input("enter the boy name :")   #taking boys name as a input
girlNm = input("enter the girl name :")     #taking girl name as a input
combinedNm = (boyNm+girlNm).lower()
T = combinedNm.count("t")
R = combinedNm.count("r")
U = combinedNm.count("u")
E = combinedNm.count("e")
first_digit = T+R+U+E
L = combinedNm.count("l")
O = combinedNm.count("o")
V = combinedNm.count("v")
E = combinedNm.count("e")
second_digit = L+O+V+E

print("your love score is "+str(first_digit)+ str(second_digit))