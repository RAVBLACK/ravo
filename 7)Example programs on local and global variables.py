# 7)Example programs on local and global variables
x = "hello"

def func():
    # Local variable
    x = "world"
    print("Local:", x)


func()

print("Global:", x)

#Output:
#Local: world
#Global: hello
