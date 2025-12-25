import numpy as np

# Define 3D arrays (shape: 2x2x2)
A = np.array([[[1, 2], 
               [3, 4]], 
               [[5, 6], 
                [7, 8]]])

B = np.array([[[1, 0], 
               [0, 1]], 
               [[1, 1], 
                [1, 1]]])

# numpy.dot on 3D arrays
dot_result = np.dot(A, B)
print("dot_result shape:", dot_result.shape)
print(dot_result)

# numpy.matmul on 3D arrays (batch matrix multiplication)
matmul_result = np.matmul(A, B)
print("matmul_result shape:", matmul_result.shape)
print(matmul_result)