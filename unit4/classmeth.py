#Example on Class method
class Student:
    college = "SNIST" 
    @classmethod
    def college_(cls): 
        print(cls.college)

s=Student()
s.college_()

#OUTPUT

