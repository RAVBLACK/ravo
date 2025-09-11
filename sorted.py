#1)Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
                        return False
        else:
                    return True

print(is_sorted([1,2,3,4,5]))
print(is_sorted([3,2,1]))
                
#Output:
#True
#False

    
