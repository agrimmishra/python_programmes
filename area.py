import math

shape = input("enter the shapes name :")
if shape == "rectangle" or shape == "square":
    height = float(input("enter the height :"))
    width = float(input("enter the width :"))
    area = height*width
    print(area)
elif shape == "triangle":
    height = float(input("enter the height :"))
    base = float(input("enter the base:"))
    area = 0.5* (height*base)
    prfloat(area)
elif shape == "circle":
    radius = float(input("enter the radius :"))
    area = math.pi * (radius**2)
    print("%.3f" %area)
elif shape == "":
    print("fill the shape name feild")
else:
    print("error")