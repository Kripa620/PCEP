import numpy as np

sample = [1,2,3,4,5,6]
print(type(sample),'\n')

#converting list into an array
sample_array = np.array(sample)
print(type(sample_array))

#create an array of zeroes
zeroes_array = np.zeros(5)
print(f'\n Zeros array: \n{zeroes_array}\n')

#create an array of one
ones_array = np.ones(7)
print(f'Ones array: {ones_array}\n')

error_array = np.array([1,2,3,'Kripalini'])
print(error_array)

#specifying data type while creating the array
float_array = np.array([1,2,3,4,5],dtype = 'f')
print(float_array,'\n')

#creating a multidimensional array
twod_array = np.array([[1,2],[3,4]])
print('\n twod_array: ')
print(twod_array,'\n')

'''
#all rows should have the same number of columns
twod_array_error = np.array([[1,2,],[3]])
print(twod_array_error)
'''

#print dimensions of an array
print('dimensions of an array: ')
print(twod_array.ndim,'\n')
