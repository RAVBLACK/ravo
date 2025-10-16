#EXAMPLE OF STATIC VARIABLE
class Student:
    college = "Snist" 
    def __init__(self, name):
        self.name = name 

student1 = Student("Shanmukha")
student2 = Student("Joyson")

print(student1.name)
print(Student.college)
print(student2.name)
print(student1.college)

#OUTPUT
#Shanmukha
#Snist
#Joyson
#Snist


