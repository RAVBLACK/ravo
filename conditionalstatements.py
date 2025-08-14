#Conditional statements

#if 
x=int(input("Enter a number: "))

if x<10:
    print("Less than 10")

#if-else
a=int(input("Enter a number: "))
if a%2==0:
      print("Even")

else:
    print("Odd")


#if-elif

x = int(input("Enter number: "))
if x<10:
    print ("given number is 1 digit number")
elif x<100:
    print ("given number is 2 digit number")
elif x<1000:
    print ("given number is 3 digit number")
else :
    print("given number is >= 4 digit number")


