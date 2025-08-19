def egl(a,b):
    if a == b:
        return "a is equal to b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is greater than b"  

print(egl(5, 5))  
print(egl(5, 10)) 
# Output: 
# a is equal to b
# a is less than b