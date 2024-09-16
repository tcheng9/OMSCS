# import numpy as np
#
# # arr = np.array([[1], [1], [1]])
# # arr2 = np.array([1,2])
# # # print(arr[arr < arr[-1])
# # val = np.corrcoef(arr2)
# # print(val)
# #
# # x_train = np.array([[1, 3, 4], [5, 3, 1], [2, 3, 1]])
# # y_train = np.array([[5, 5,7],])
# # print(x_train)
# # print(y_train)
# #
# # np.concatenate((x_train, y_train), axis =1)
# # # np.corrcoef(x_train, y_train)
#
# arr = np.array([[2,3], [4,5], [3, 5]])
# arr2 = np.array([[1], [2], [3]])
# arr2 = np.reshape(arr2, (-1, 1))
#
# np.corrcoef((arr, arr2))

import random
import numpy as np
random.seed(10)
print(random.randint(1, 10))

arr = np.array([[1]])
print(arr.shape)