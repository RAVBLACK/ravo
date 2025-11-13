#tell()
with open("rav.txt", "r") as file:
    print(file.tell()) 
    data = file.read(5) 
    print(data)
    print(file.tell())

#OUTPUT:
#0
#hey
#y
#6
