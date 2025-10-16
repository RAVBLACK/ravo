#EXAMPLE ON LOCAL VARIABLE
class Student:
    def calculate_grade(self, marks):
        
        if marks > 90:
            grade = "A"
        else:
            grade="B" 
        return grade

student = Student()
print(student.calculate_grade(80))
print(student.calculate_grade(95))

#OUTPUT:
#B
#A
