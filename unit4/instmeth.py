#Example on instance method
class Student:
    def __init__(self,college):
        self.college =college

    def greet(self):
            print(f"Hello!! You are in {self.college}")

s=Student("SNIST")
s.greet()

#OUTPUT
#Hello!! You are in SNIST

