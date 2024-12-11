# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
def compair(a, b):
    if(a>b):
        return a
    else:
        return b

l = [1,2,33,44,56,79,4,34,664,64,22,90]

print(reduce(compair,l))
