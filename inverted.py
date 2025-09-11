#5)Write a python code to read a dictionary values from the user. Construct a function to invert its content. i.e., keys should be values and values should be keys.

def invert_dict(d):
    return{value:key for key,value in d.items()}

n=int(input("How many key value pairs?"))

input_dict={}
for i in range(n):
    key=input(f"Enter key #{i+1}:")
    value=input(f"Enter the value for key '{key}':")
    input_dict[key]=value

inverted=invert_dict(input_dict)
print("Inverted dictionary:",inverted)


#Output:
#How many key value pairs?3
#Enter key #1:1
#Enter the value for key '1':one
#Enter the value for key '2':two
#Enter key #3:3
#Enter the value for key '3':three
#Inverted dictionary: {'one': '1', 'two': '2', 'three': '3'}