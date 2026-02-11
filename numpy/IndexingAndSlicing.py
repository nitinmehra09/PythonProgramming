import numpy as np
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
arr = np.array(a)
print(f"element at 3 index = {a[1]}")

# slicing
print(f"First 3 element {arr[:1]}")

arr2d = np.array([a,b,c])

print(f"2D array - \n{arr2d}")
print(arr2d[1:3,1:3])

a = arr[arr>10]
print(a)

# multiple conditions 
a = arr[(arr>5) & (arr<25)]
print(a)

a = np.where(arr>10,True,False)
print(a)

print(arr.size)
print(arr.ndim)
print(arr2d.size)
print(arr2d.ndim)