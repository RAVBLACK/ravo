#program using Append mode

file=open("newfile.txt","a")
file.write("This is a new line added to the file.\n")
file.write("Apending another line.\n")
file.close()
