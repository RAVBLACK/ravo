#3)Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original. Hint: they don’t have to be in the same order.

def remove_dup(lst):
    return list(set(lst))
nums=[1,2,2,3,4,4,5]
result=remove_dup(nums)
print(result)

#Output:
#[1, 2, 3, 4, 5]