def getName(id) :
    planet = {1: "Mercury",2:"v",3:"E",4:"M",5:"J",6:"S",7:"U",8:"N"}
    name = planet[id]
    return name
    
name_output = getName(8)
print(name_output)