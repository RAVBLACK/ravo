#Seek()

with open('rav.txt','r') as f:
    data = f.read(10)
    print(data)

    print("Current position:",f.tell())
    f.seek(0)
    print("position of pointer after seek:", f.tell())
