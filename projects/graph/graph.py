"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return self.vertices

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error adding edge: vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return  self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
         -- FIFO --
        """
        my_queue = Queue()
        my_queue.enqueue(starting_vertex)

        visited = set()
        while my_queue.size() > 0:
            current_node = my_queue.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)

                neighbors = self.get_neighbors(current_node)
                for i in neighbors:
                    my_queue.enqueue(i)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        my_stack = Stack()
        my_stack.push(starting_vertex)
        visited = set()
        while my_stack.size() > 0:
            current_node = my_stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
                for i in neighbors:
                    my_stack.push(i)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                self.dft_recursive(i, visited)
                


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        my_queue = Queue()
        my_queue.enqueue([starting_vertex])
        # print('my_queue', my_queue.queue)
        visited = set()
        while my_queue.size() > 0:
            print('my_queue', my_queue.queue)
            current_path = my_queue.dequeue()

            if current_path[-1] not in visited:
                if current_path[-1] == destination_vertex:
                    return current_path
                visited.add(current_path[-1])
                print('current_path',current_path)
                print('visited',visited)
                neighbors = self.get_neighbors(current_path[-1])
                for i in neighbors:
                    new_path = list(current_path)
                    print('new_path1', new_path)

                    new_path.append(i)
                    print('new_path2', new_path)
                    my_queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        my_stack = Stack()
        my_stack.push([starting_vertex])
        visited = set()
        while my_stack.size() > 0:
            current_path = my_stack.pop()
            if current_path[-1] not in visited:
                if current_path[-1] == destination_vertex:
                    return current_path
                visited.add(current_path[-1])

                for i in self.get_neighbors(current_path[-1]):
                    path = list(current_path)
                    path.append(i)
                    my_stack.push(path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
        # Track visited Nodes
        visited.add(starting_vertex)
        new_path = list(path) + [starting_vertex]
        #  Base Case
        if starting_vertex == destination_vertex:
            return new_path
        # print(starting_vertex)

        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                neighbor_path = self.dfs_recursive(i, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(4)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('1', graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))


    # graph.dft_recursive(1)