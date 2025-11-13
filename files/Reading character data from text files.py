#Reading character data from text files

a = open('rav.txt', 'r')
data = a.read()
print("The contents of the file are:")
print(data)
a.close()

