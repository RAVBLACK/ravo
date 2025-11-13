#Using WITH
with open("newfile.txt", "r") as file:
    data = file.read()
print(data)

#OUTPUT:
#This file was created using 'x' mode.This is a new line added to the file. Apending another line.
