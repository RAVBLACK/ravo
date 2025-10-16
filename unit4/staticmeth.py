#Example on Static method
class Student:
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

Student.greet("Steve")

#OUTPUT
#Hello, Steve!
