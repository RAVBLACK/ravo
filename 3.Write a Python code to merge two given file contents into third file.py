#3.Write a Python code to merge two given file contents into third file.

f1=open('example1.txt','r')
f2=open('example2.txt','r')
mfile=open('merge.txt','w')
data1=f1.read()
data2=f2.read()
mfile.write(data1)
mfile.write(data2)
f1.close()
f2.close()
mfile.close()
