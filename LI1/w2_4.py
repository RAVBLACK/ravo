#4)Write a program to print GRADE obtained by a student using the following RULE.
#Above 75          O
#60-75                 A
#50-60                 B
#40-50                 C
#Less than 40     D

grade=int(input("Enter your grade: "))
if grade >= 75:
    print("You have recieved O grade")
elif grade >= 60 & grade < 75:
    print("You have recieved A grade")
elif grade >= 50 and grade < 60:
    print("You have recieved B grade")
elif grade >= 40 and grade < 50:
    print("You have recieved C grade")
else :
    print("You have recieved D grade")

#output:
# Enter your grade: 85
# You have recieved O grade
# Enter your grade: 65
# You have recieved A grade
# Enter your grade: 55
# You have recieved B grade
# Enter your grade: 45
# You have recieved C grade
# Enter your grade: 35
# You have recieved D grade
