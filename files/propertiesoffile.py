#Various properties of file object

a= open('rav.txt','r')
print('file Name:',a.name)
print('file mode:',a.mode)
print('Is file Readable:',a.readable())
print('Is file writable:',a.writable())
a.close()
print('Is file closed:',a.closed)
