
with open("file.txt", "w") as f:
    f.write("Hello World")

with open("file.txt", "r") as f:
    print( f.read())

with open("file.txt", "r+") as f:
    f.write("Welcome to Python")

with open("file.txt", "w+") as f:
    f.write("Python is easy")
    f.seek(0)  
    print( f.read())



