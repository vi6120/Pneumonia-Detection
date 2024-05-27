# Numpy Code Example

# 
# Here is a simple example of how to use Numpy to create 
# an array and perform basic operations on it
#

import numpy as np

# Version Check:
print(numpy.__version__)

# Example 1

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4])

# Perform operations on the array
print(arr + 1) # [2, 3, 4, 5]
print(arr * 2) # [2, 4, 6, 8]

# Example 2:

#
# Here is another example of how to use Numpy to create 
# a 2-dimensional array and perform more
# advanced operations on it
#

import numpy as np

# Create a 2-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Perform operations on the array
print(arr.shape)  # (2, 3)
print(arr.mean()) # 3.5

# Example - Files

#
# You can save and load numpy array into a file with numpy functions 
# such as follows: "numpy.save" and "numpy.load"
#

arr = np.array([1, 2, 3, 4])
np.save('my_array', arr)
loaded_array = np.load('my_array.npy')