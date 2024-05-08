# test_set = {}
# print(test_set)
#
# test_set.add((4,4))
# test_set = set((4,4))
# test_set.remove((4,4))
# print(test_set)
#
# test_set.add((6,6))
# print(test_set)
#
# test_set.remove((6,6))
# print(test_set)

# test_set = set()
# print(test_set)
#
# test_set.add((4,4))
# print(test_set)
#
#
# open_set = set()
# print(open_set)
# open_set.add((4,4))
# print(open_set)
#


# s = 'a'
# s = '#'
#
# print(s.isalnum())
#
#
# motion_dict = {
#             (-1, 0): 'n',  # (row, col)
#             (1, 0):'s',
#             (0, 1):'e',
#             (0, -1): 'w',
#             (-1, -1): 'nw',
#             (-1, 1) : 'ne',
#             (1, -1):'sw',
#             (1, 1): 'se'
#         }
#
# for i in motion_dict.keys():
#     print(i)

# s = 'abcdef'
#
# print(s[6:])
# s = s[6:]
# if s == '':
#     print('true')
# else:
#     print('false')

# arr = [1,2,3,4]
# arr.pop()
# print(arr)

# arr = [1,2]
#
# counter = 0
# while counter < len(arr):
#     print(counter)
#     counter += 1

#
# warehouse_viewer = [
#     '#############',
#     '#.....@...J1#',
#     '#############',
# ]
#
# curr_x = 1
# curr_y = 1
# res = []
# # print(warehouse_viewer[0][0])
#
#
# for i in range(len(warehouse_viewer)):
#     s = '.'
#     for j in range(len(warehouse_viewer[0])):
#         if i == curr_x and j == curr_y:
#             s += 'x'
#         s += warehouse_viewer[i][j]
#     res.append(s)
#
# print(res)
#
# # print(warehouse_viewer[i][j])
# # warehouse_viewer[i][j] = '0'
#
#
# warehouse_viewer = [
#     '#######################',
#     '#........#####.......@#',
#     '#.......##...##.....x.#',
#     '#.....###...I.###..x..#',
#     '#....##..#...#..##x...#',
#     '#..##............x##..#',
#     '#...##..#.....#..##...#',
#     '#...##...#...#...##...#',
#     '#....#....###....#....#',
#     '#....#..........##....#',
#     '#.....###########.....#',
#     '#1....................#',
#     '#######################'
# ]
#
# print(len(warehouse_viewer))
# print(len(warehouse_viewer[0]))
# print(warehouse_viewer[3][12])

s = 'abcdef'

if 'a' in s:
    print('true a ')

if 'F' in s:
    print('trueF')

warehouse_viewer = [
    '#############',
    '#.....@...J1#',
    '#############',
]

# print(len(warehouse_viewer))
# print(len(warehouse_viewer[0]))


warehouse_viewer = [
    '###########',
    '#....1....#',
    '#....###..#',
    '#...##.##.#',
    '#..##.....#',
    '###.#..#.##',
    '#..##..#..#',
    '#...#####.#',
    '#.#..#@...#',
    '#.........#',
    '###########'
]
todo = list('1@')

for i in range(len(warehouse_viewer)):
    for j in range(len(warehouse_viewer[0])):
        if warehouse_viewer[i][j] in todo:
            print(warehouse_viewer[i][j], 'is at', i, j)


# [27, 9, 18, 9, 3, 8, 4],, [25, 7, 18, 9, 3, 9, 4]