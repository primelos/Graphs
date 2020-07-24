# adjacency list
class Graph:
    def __init__(self):
        self.vertices = {
            'A':{'B':1},
            'B':{'C':3, 'D':2, 'E':1},
            'C':{'E':4},
            'D':{'E':2},
            'E':{'F':3},
            'F':{},
            'G':{'D':1}
        }

# adjacency matrix
class Graph:
    def __init__(self):
        self.edges = [
        #    a b c d e f g
            [0,1,0,0,0,0,0],
            [0,0,3,2,1,0,0],
            [0,0,0,0,4,0,0],
            [0,0,0,0,3,0,0],
            [0,0,0,0,0,3,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0]
        ]
