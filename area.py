import math

shape = input("enter the shapes name :")
if shape == "rectangle" or shape == "square":
    height = int(input("enter the height :"))
    width = int(input("enter the width :"))
    area = height*width
    print(area)
elif shape == "triangle":
    height = int(input("enter the height :"))
    base = int(input("enter the base:"))
    area = 0.5* (height*base)
    print(area)
elif shape == "circle":
    radius = int(input("enter the radius :"))
    area = math.pi * (radius**2)
    print(area)
elif shape == "":
    print("fill the shape name feild")
else:
    print("error")