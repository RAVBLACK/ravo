#4)Example program on filter()

lt = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, lt))
print(even)

#Output:
#[2, 4, 6]
