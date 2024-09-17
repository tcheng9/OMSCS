import numpy as np

arr = np.array([])
arr1 = np.array([1])
end = np.append(arr, arr1) #arr1 = main array to use, arr are values you want to append
end = np.append(end, arr1)
end = np.append(end, arr1)
print(end)

print(end.reshape(-1, 1))