import re

pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
email = input("enter email :")
if pattern.match(email):
    print("email is valid")
else:
    print("email is not valid")