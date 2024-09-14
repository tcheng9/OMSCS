import numpy as np

# arr = np.array([[1], [1], [1]])
# arr2 = np.array([1,2])
# # print(arr[arr < arr[-1])
# val = np.corrcoef(arr2)
# print(val)

x_train = np.array([[1, 3, 4], [5, 3, 1], [2, 3, 1]])
y_train = np.array([[5, 5,7],])
print(x_train)
print(y_train)

np.concatenate((x_train, y_train), axis =1)
# np.corrcoef(x_train, y_train)
