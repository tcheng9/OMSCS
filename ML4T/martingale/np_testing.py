import numpy as np

arr = np.array([[2,4,6],
                [1,3,10],
                [0,2,4]]
               )
print(np.median(arr, axis = 0))