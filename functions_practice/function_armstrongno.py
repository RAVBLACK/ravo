def armstrong(x):
    sum = 0
    temp = x
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == x:
        return "Armstrong"
    else:
        return "Not Armstrong"
    
print(armstrong(153))  
# Output: Armstrong
print(armstrong(123))  
# Output: Not Armstrong
