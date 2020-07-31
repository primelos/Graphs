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


# 2. Build a Graph

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    def size(self):
        return len(self.vertices)

def build_graph(ancestors):
    gg = Graph()
    for parent, child in ancestors:  #tuple unpacking
        gg.add_vertex(parent)
        gg.add_vertex(child)
        gg.add_edge(child, parent)
    return gg

def earliest_ancestor(ancestors, starting_node):
    
# using DFS
# Nodes -> people
# Edges -> when a child has a parent.
    gg = build_graph(ancestors)

    ss = Stack()
    visited = set()
    ss.push([starting_node])
    longest_path = [starting_node]
    aged_one = -1

    while ss.size() > 0:
        path = ss.pop()
        current_node = path[-1]

        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            print('longest_path',longest_path)
            aged_one = longest_path[-1]
            print('aged_one', aged_one)
        
        if current_node not in visited:
            
            # print(current_node)
            visited.add(current_node)
            parents = gg.get_neighbors(current_node)
           
            for parent in parents:
                new_path = path + [parent]
                ss.push(new_path)
            

    return aged_one


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,3))