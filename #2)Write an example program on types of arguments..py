#2)Write an example program on types of arguments.
#a)positional
#b)keyword
#c)default
#d)variable length
    #i)args
    #ii)kwargs

#Positional argument
def  person(name, age):
    print(f"Name: {name}, Age: {age} ")

person("Karthik", 19)

#Output:
#Name: Karthik, Age: 19


#Keyword argument

person(age=19, name="Sainath")

#Output:
#Name: Sainath, Age: 19 


#default argument
def greet(name, age=18):
    print(f"Name: {name}, Age: {age}")

greet("Bhanu")

#Output:
#Name: Bhanu, Age: 18


#Variable length
#i)args

def add(*args):
    print("Sum:", sum(args))

add(4,3,2,1)

#Output:
#Sum: 10


#ii)kwargs

def print_(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_(Name="Rakesh", Age=19)

#Output:
#Name: Rakesh
#Age: 19

