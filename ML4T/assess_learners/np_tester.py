import numpy as np

# class test case
x_train = np.array([
    [.885, .330, 9.1],
    [.725, .39, 10.9],
    [.560, .5, 9.4],
    [.735, .570, 9.8],
    [.610, .630, 8.4],
    [.260, .630, 11.8],
    [.5, .68, 10.5],
    [.320, .780, 10]

])

y_train = np.array([4, 5, 6, 5, 3, 8, 7, 6])

subsample_x = np.matrix([])
y_subsample = np.array([])

# random_index = np.random.randint(0, x_train.shape[0])
subsample_x = np.empty((0, x_train.shape[1]))
subsample_y = np.array([])
for i in range(10):
    random_row = np.random.randint(0, x_train.shape[0])

    print('random index is', random_row)

    subsample_x = np.vstack((subsample_x, x_train[random_row, :]))
    subsample_y = np.append(subsample_y, y_train[random_row])
print(subsample_x)
print(subsample_y)
#
# # Step 1: Create an empty matrix with shape (0, 5) - 0 rows and 5 columns
# empty_matrix = np.empty((0, 5))
#
# # Step 2: Create a 1-row, 5-column matrix to append
# new_row = np.array([[1, 2, 3, 4, 5]])
#
# # Step 3: Append the new row to the empty matrix
# result_matrix = np.vstack((empty_matrix, new_row))
#
# print(result_matrix)