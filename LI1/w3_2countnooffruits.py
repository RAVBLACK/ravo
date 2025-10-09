#2)Write a program to count how many times each fruit
#appears using dictionary?
#fruits = ["apple", "banana", "apple", "cherry","banana", "apple"]

fruits = ["apple", "banana", "apple", "cherry","banana", "apple"]
count={}

for i in fruits:
    count[i]=count.get(i,0)+1

print(count)

#output:
# {'apple': 3, 'banana': 2, 'cherry': 1}