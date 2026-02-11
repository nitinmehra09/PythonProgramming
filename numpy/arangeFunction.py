import numpy as np
arr = np.arange(1,9,2)
print(arr)

# arr = arr.reshape(3,3)
# print(arr)

# random functions
arr = np.random.rand(10)
print(arr)
arr = np.random.randint(1,10,(3,3))
print(arr)

arr = np.random.randn(4)
print(arr)

arr = np.array([1,2,10,3,4,5])
ans = np.all(arr<5)
print(ans)

ans = np.argmax(arr)
print(ans)