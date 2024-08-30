import numpy as np
import matplotlib.pyplot as plt
arr = np.array([[1,2,3, 4]])
print(arr.shape)

arr0 = np.array([[0], [0]])
print(arr0.shape)
arr1 = np.array([[1],[2],[3]])
print(arr1.shape)


# total_results = np.array([[2,4,6],
#                 [1,3,10],
#                 [0,2,4]]
#                )
#
#
#
# median_per_round = np.median(total_results, axis = 0)
# median_per_round = median_per_round.transpose()
#
#
# plt.plot(median_per_round)
# plt.title('figure 2')
# # plt.plot(std_per_round_pos[0, :])
# # plt.plot(std_per_round_neg[0, :])
#
# plt.show()


total_results = np.array([[12,14,16],
                [11,13,10],
                [10,12,14]]
               )



median_per_round = np.median(total_results, axis = 0)
median_per_round = median_per_round.transpose()

plt.plot(median_per_round)
plt.title('figure 3')
# plt.plot(std_per_round_pos[0, :])
# plt.plot(std_per_round_neg[0, :])

plt.show()
