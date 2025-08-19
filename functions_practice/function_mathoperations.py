def mathop(a,b):
    return a + b, a - b, a * b, a / b if b != 0 else "Division by zero is not allowed"

print(mathop(10, 5))
# Output: (15, 5, 50, 2.0)
print(mathop(10, 0))        
# Output: (10, 10, 0, "Division by zero is not allowed")