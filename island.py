# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]


# def check_islands(islands):
#     island_check = [[False for x in range(len(islands[y]))] for y in range(len(islands))]
#     print(island_check)
#     all_islands = []

#     for y in range(len(islands)):
#         for x in range(len(islands[y])):
#             if not island_check[y][x] and islands[y][x] == 1:
#                 current_group = [[x, y]]
#                 i = 0
#                 while i < len(current_group):
#                     x_current = current_group[i][0]
#                     print('x_current', x_current)
#                     y_current = current_group[i][1]
#                     island_check[y_current][x_current] = True
#                     if x_current > 0:
#                         print('x_current2', x_current)
#                         print('islands[y_current][x_current-1]', islands[y_current][x_current-1])
#                         if islands[y_current][x_current-1] == 1 and not island_check[y_current][x_current-1]:
#                             current_group.append([x_current-1, y_current])
#                     if x_current < len(islands[y_current])-1:
#                         if islands[y_current][x_current+1] == 1 and not island_check[y_current][x_current+1]:
#                             current_group.append([x_current+1, y_current])
#                     if y_current > 0:
#                         if islands[y_current-1][x_current] == 1 and not island_check[y_current-1][x_current]:
#                             current_group.append([x_current, y_current-1])
#                     if y_current < len(islands)-1:
#                         if islands[y_current+1][x_current] == 1 and not island_check[y_current+1][x_current]:
#                             current_group.append([x_current, y_current+1])   
#                     i += 1
#                 all_islands.append(current_group)
#     return all_islands
           

                   
# print(check_islands(islands))



class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:
        print('matrix[x]', x)
        print('matrix[x-1]',matrix[x-1])
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        print('matrix[y]', matrix[y])
        print('matrix[y-1]',matrix[y-1])
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors


def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    # print('s',s.stack)
    while s.size() > 0:
        v = s.pop()
        # print('v[1]',v[0],v[1])
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
        # print('visited', visited)
    island_count = 0
    for x in range(len(matrix[0])):
        print(x)
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count

def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))


matrix = [
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 1], 
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 0], 
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0], 
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], 
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 0], 
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], 
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
print_matrix(matrix)
print(island_counter(matrix))