#4)Convert Tuple to List and List to Tuple.
l=[1,2,3,4,5]
print("In list form : " ,l)
res=tuple(l)
print("In tuple form: ",res) #prints tuple

t=(9,8,7,6)
print("In tuple form",t)
res2=list(t)
print("In list form",res2)

#Output:
#In list form :  [1, 2, 3, 4, 5]
#In tuple form:  (1, 2, 3, 4, 5)
#In tuple form:  (9, 8, 7, 6)
#In list form:  [9, 8, 7, 6]
