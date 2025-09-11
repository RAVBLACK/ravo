#2)Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list in python.

def has_duplicate(lst):
    seen=set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
        return False

print(has_duplicate([1,2,3,4]))
print(has_duplicate([1,2,3,1]))
print(has_duplicate(['a','b','a']))
print(has_duplicate([]))

#Output:
#False
#False
#False
#None