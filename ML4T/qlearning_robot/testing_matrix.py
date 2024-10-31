import numpy as np

# Define a 3x3x3 matrix
matrix_3d = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

# print(matrix_3d)
print(matrix_3d[0])
print(np.sum(matrix_3d[0]))