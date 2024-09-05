student_record={}
for i in range (0,2):
    name = input("enter name")
    math = int(input("enter maths marks :"))
    mathp = int(input("enter maths marks :"))
    student_record[name] = {"math":math,"physics": mathp}
    for key in student_record:
        print(f"name:{key}\nmath:{student_record[key]["math"]}\n")