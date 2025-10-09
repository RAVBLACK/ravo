#3)Write a program to find SUM of N natural Number?
n=int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i    
print("The sum of the first", n, "natural numbers is:", sum)

#output:
# Enter a number: 5
# The sum of the first 5 natural numbers is: 15