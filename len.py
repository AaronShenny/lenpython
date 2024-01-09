def len3(value):
    if isinstance(value,int):
        num = 0
        while value>0:
            value = value//10
            num = num + 1
        
    elif isinstance(value,str):
        if hasattr(value, "__len__"):
            return value.__len__()  # Calls the __len__() method of the object
        else:
            raise TypeError("Object of type {} has no len()".format(type(value)))
    else:
        if hasattr(value, "__len__"):
            return value.__len__()  # Calls the __len__() method of the object
        else:
            raise TypeError("Object of type {} has no len()".format(type(value)))
    return num

value = input('Enter a value : ')
if value[0] == '[' or  value[0] == '(':
    value = eval(value)
len1 = len(value)
print(len1)