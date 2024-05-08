# '''
# arr = [[0,1,2], [3,4,5], [6,7,8], [9,10,11]]
# newArr = [[0.0 for i in range(len(arr[0]))] for j in range(len(arr))] #for each row, create a column array
# # newArr = [0] * len(arr)
# # move = 1
# # for i in range(len(arr)):
# #     newArr[i] = arr[(i-move % len(arr))]
#
# #print(newArr)
#
# row = len(arr)
# col = len(arr[0])
# move = 1
# ###########X-axis movement
# for r in range(row):
#     for c in range(col):
#         newArr[r][c] =  arr[r][(c - move) % len(arr[0])]
#
# #print(newArr)
#
# ###########Y-axis movement
# for r in range(row):
#     newArr[r] = arr[(r-move) % len(arr)]
#
# print(newArr)
#
#
#
#
# motions = [-1,1]
# x,y = motions
# print(x,y)
# '''
#
#
#
#
#
# #################################Testing my actual problem set code
motions = [0,1]
# p = [[0.1, 0.02464, 0.06799, 0.04472, 0.02465],
#                                           [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#                                           [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#                                           [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
p = [[0,1,2],[3,4,5]]
y, x = motions
newArr = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]

# newArr = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]
row = len(p)
col = len(p[0])

p_move = .8
p_still = 1 - p_move

# for r in range(row):
#     newArr[r] = p[(r - y) % row]
#     print((r - y) % row)
#     for c in range(col):
#         newArr[r][c] = p[r][(c - x) % col]
#     print('c', (c - x) % col)
aux = 0
#######Column movement
for r in range(row):
    aux = p[(r - y) % row]
    newArr[r] = aux
# print(p)
# row movement??
for r in range(row):
    for c in range(col):
        print(r, (c - x) % col)
        # newArr[r][c] = p[r][(c - x) % col]
        # print(r,(c - x) % col)
print(newArr)



#######Row movement
# for r in range(row):
#     newArr[r] = p[(r - y) % row]
# ########column movement
#     # print('row swap iter:', p)
#     # print((r - y) % row)
#     print('r', p)
#     for c in range(col):
#         # print(p[r][(c - x) % col])
#         # print(p[r][(c - x) % col])
#
#         print('inner')
#         newArr[r][c] = p[r][(c - x) % col]
#
#         # print(p[r][(c - x) % col])
#         # print(p)
#         # continue
# # #         print(r,c)
# print(newArr)
# print(newArr)
# #######Column movement
# for r in range(row):
#     newArr[r] = p[(r - y) % row]



# print(newArr)



#
