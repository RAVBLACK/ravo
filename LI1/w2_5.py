#5)Write a program to find whether a given year is Leap year or Not.
year=int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#output:
# Enter a year: 2020    
# 2020 is a leap year.