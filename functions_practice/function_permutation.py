def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i   
    return fact

def permutation(n, r):
    return fact(n) // fact(n - r)

print(permutation(5, 2))
# Output: 20