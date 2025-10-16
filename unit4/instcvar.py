#EXAMPLE OF INSTANCE VARIABLE
class Student:

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

student1 = Student("Shanmukha", 19)
student2 = Student("Joyson", 19)

print(student1.name)
print(student1.age) 
print(student2.name) 
print(student2.age) 

#OUTPUT
#Shanmukha
#19
#Joyson
#19
