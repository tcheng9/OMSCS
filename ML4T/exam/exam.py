import pandas as pd
import numpy as np

x = np.array([[1,2,3],[5,6,7]], dtype='int')
y = np.array(x/2)
x[1,0] = 0
print(y.sum(axis=1)[-1])