"""Create a 3D NumPy array with shape (2, 3, 2) containing consecutive odd numbers starting from 1.
Hint: - look at the reshape method"""

#Solution

import numpy as np

# Calculate the total number of elements in the 3D array
total_elements = 2 * 3 * 2

# Create a 1D array of consecutive odd numbers starting from 1
consecutive_odd_numbers = np.arange(1, total_elements*2, 2)

# Reshape the 1D array into a 3D array with shape (2, 3, 2)
array_3d = consecutive_odd_numbers.reshape(2, 3, 2)

print(array_3d)
