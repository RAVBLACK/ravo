#1. Write a Python program to demonstrate the usage of MRO in multiple levels of inheritances.
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")

class D(B,C):
    pass

d=D()
d.show()

print("MRO of Class D:")
for cls in D.__mro__:
    print(cls)

#OUTPUT:
#Class B
#MRO of Class D:
#<class '__main__.D'>
#<class '__main__.B'>
#<class '__main__.C'>
#<class '__main__.A'>
#<class 'object'>


