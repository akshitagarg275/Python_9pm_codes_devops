
# pip install numpy

import numpy as np

# creating a 1D array
arr1 = np.array([1,2,3,4,5,6])
# print(arr1)
# print(type(arr1))

# creating a 2D array
arr2 = np.array([[1,2,3], [4,5,6]])
# print(arr2)
# print(type(arr2))

# ERROR
# res = arr1 + arr2
# print(res)

# print(np.ones((2,3)))
# print(np.zeros((2,3)))

# arr = np.arange(10)
# print(arr)

# arr = np.arange(5,15,2)
# print(arr)

# arr = np.array([1,2,3,4,5])
# total = np.sum(arr)
# print(total)

# mean = np.mean(arr)
# print(mean)

# dot(a,b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# dot_product = np.dot(arr1,arr2)
# print(dot_product)

# arr_linspace1 = np.linspace(0,1,5)
# print(arr_linspace1)

# arr_random = np.random.rand(3,3)
# print(arr_random)


# arr = np.array([1,2,3,4,5])
# indices = np.where(arr > 2)
# print(indices)

# arr = np.arange(12)
# reshaped_arr = np.reshape(arr ,(3,4) )
# print(reshaped_arr)

arr = np.array([5,2,8,1, 10])
min_val = np.min(arr)
max_val = np.max(arr)

print("min val: ", min_val)
print("max val: ", max_val)
print("Index of min value: ", np.argmin(arr))
print("Index of max value: ", np.argmax(arr))


# arr = np.array([10, 5, 30, 20 , 15])
# sorted_indices = np.argsort(arr)
# print(sorted_indices)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)
