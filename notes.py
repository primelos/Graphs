# # adjacency list
# class Graph:
#     def __init__(self):
#         self.vertices = {
#             'A':{'B':1},
#             'B':{'C':3, 'D':2, 'E':1},
#             'C':{'E':4},
#             'D':{'E':2},
#             'E':{'F':3},
#             'F':{},
#             'G':{'D':1}
#         }

# # adjacency matrix
# class Graph:
#     def __init__(self):
#         self.edges = [
#         #    a b c d e f g
#             [0,1,0,0,0,0,0],
#             [0,0,3,2,1,0,0],
#             [0,0,0,0,4,0,0],
#             [0,0,0,0,3,0,0],
#             [0,0,0,0,0,3,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,1,0,0,0]
#         ]


x = [
    [0,  1,  2,  3,  4],
    [5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
    ]
# print((x))
for i in range(len(x[0])):
    # print(i)
    for j in range(len(x[0])):
        print(x[i][j])

       