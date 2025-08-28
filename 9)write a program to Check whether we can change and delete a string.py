#9)write a program to Check whether we can change and delete a string

s1 = "Hello"
s2 = 'h' + s1[1:]
print("New string:", s2)
del s1

print(s1)
#Output:
#New string: hello
