n=int(input("Enter a number to find its factorial: "))
f = 1
for i in range(1, n + 1):
    f *= i  
print("The factorial of", n, "is:", f)

