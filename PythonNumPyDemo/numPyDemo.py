# NumPy is a fundamental library for scientific computing in python
# it provides support for arrays in matrices along with a collection of mathematical
# functions to operate on these data structures


import numpy as np

# create an array using numpy

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr3 = np.array([[1,2,3,4,5], [2,3,4,5,6]]) # list inside of a list
#print(type(arr1))
#rint(arr1)
#print(arr1.shape)
#arr1.reshape(1,5)
#arr2.reshape(1,5)
#print(arr3)
#print(arr3.shape)

np.arange(0,10,2).reshape(5,1)