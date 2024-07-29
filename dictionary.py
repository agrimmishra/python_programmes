my_dict = {}
word = input("enter word :")
meaning = input("enter the meaning :")
my_dict[word] = meaning
for word , value in my_dict.items():
    print(f"{word} : {value}")

