import numpy as np

py_2dim_list = [[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]]

# Create a 2D numpy array
np_2dim_array = np.array(py_2dim_list)

print(np_2dim_array)

# Print the details of the array (dimensions, shape, size, and datatype)
print("Dimensions: ", np_2dim_array.ndim)
print("Shape: ", np_2dim_array.shape)
print("Size: ", np_2dim_array.size)
print("Date Type: ", np_2dim_array.dtype)


# Perform indexing and slicing operations to access specific elements and slices of the array
print("Second Index: ", np_2dim_array[2])
print("Slice of index 2 to 4", np_2dim_array[0, 2:4])

# Reshape the array from (3, 4) to (4, 3).  
print("Reshaped Array", np_2dim_array.reshape(4, 3))