#6)write a program to print reverse of a number?
x=int(input("Enter a number: "))
num = 0
while x > 0:
    digit = x % 10
    num = num * 10 + digit
    x //= 10    
print("The reversed number is:", num)

#output:
# Enter a number: 12345 
# The reversed number is: 54321
