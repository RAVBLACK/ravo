#6)Example program on reduce()

from functools import reduce

lt = [1, 2, 3, 4]
summ = reduce(lambda x, y: x + y, lt)
print(summ)

#Output:
#10
