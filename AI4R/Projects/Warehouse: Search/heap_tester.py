# # from heapq import heapify, heappop, heappush
# # arr = [(15,2,3,4,5), (9,8,7,5,4), (11, 3,5,7,8)]
# #
# # heapify(arr)
# #
# # print(arr)
# #
# # for i in range(len(arr)):
# #     arr[1] = ['test']
# #
# # print(arr)
#
# for i in range(3):
#     print('i', i)
#     for j in range(4):
#         if j == 2:
#             continue
#         print('i', i, 'j', j)
#
#
#
#
# ##
# arr = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
# probabilties = [.05, .1, .7, .1, .05]
# for i in range(len(arr)):
#     #for each direction
#     s_motions = ''
#     for j in range(-2, 3):
#         print(arr[(i + j) % len(arr)])
#         print(probabilties[j+2])
#         # print()
#     print('----------')
#f,g,h
from heapq import heapify, heappop, heappush

arr = [[10, 5, 3], [13, 3, 7], [15, 8, 10], [5,2,3], [10,5,4]]
heapify(arr)
print(arr)
# new_arr = [10, 4, 2]
for i in range(len(arr)):
    # print(arr[i])
    if i == 2:
        arr[i] = [0, 0, 0]

    print(arr)
    heapify(arr)

