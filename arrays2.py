import numpy as np

#reshape a linear array to a required dimension
reshaped_array = np.arange(1,10).reshape(3,3)
print('reshaped_array: ')
print(reshaped_array, '\n')
print('Reshaped arr shape = ', reshaped_array.shape, '\n')

linear_array = np.arange(1,37)
print("reshape array (6 rows, 6 columns)= \n ", linear_array.reshape(6,6), '\n')
#while reshaping an array, the total number of items should remain the same
print("reshaped array (12 rows, 3 columns) = \n", linear_array.reshape(12,3),'\n')
print("reshaped array (9 rows, 4 columns) = \n", linear_array.reshape(9,4),'\n')

random_array = np.random.permutation(np.arange(1,11))
print(random_array)
sorted_array = np.sort(random_array)
print("sorted array = ", sorted_array, '\n')
