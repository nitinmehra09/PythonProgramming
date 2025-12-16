import numpy as np
a = [10,20,30,40,50]
b = [11,22,33,44,55]
c = [1,2,3,4,5]
arr = np.array([a,b,c])

print(arr)
print(type(arr))

zero = np.zeros((2,3))
print(zero)

one = np.ones((4,2))
print(one)

a = np.linspace(0,1,10)
print(a)

e = np.eye(3)
print(e)