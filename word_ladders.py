# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
import string


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# start word: 'hit'
# end word = 'cog'
# return: ['hit', 'hot', 'cot', 'cog']

# STEP 1: graph terminology

# STEP 2: build the graph
## Read in words
f = open('words.txt', 'r')
words = f.read().split('\n')
# print(words)
f.close()
word_set = set()
for word in words:
    word_set.add(word.lower())

# get neighbors and vertices 
def get_neighbors(word):
    neighbors = []
    # for every letter in the word
    for i in range(len(word)):
    # for every letter in the alphabet
        for alpha_letter in string.ascii_lowercase:
    # swap out the word-letter with the alphabet-letter
    # turn into list
            word_list = list(word)
            word_list[i] = alpha_letter
            print(word_list)
    # turn word list back into a string
            maybe_neighbor = ''.join(word_list)
            # print(maybe_neighbor)
            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)
                # print(neighbors)
    return neighbors

# STEP 3 : choose algorithm -> BFS 

def find_ladders(start_word, end_word):    # or def bfs(start_word, end_word):
    qq = Queue()
    visited = set()
    qq.enqueue([start_word])

    while qq.size() > 0:
        current_path = qq.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path
        if current_word not in visited:
            # print(current_word)
            neighbors = get_neighbors(current_word)
            visited.add(current_path[-1])
            for neighbor in neighbors:
                path_copy = list(current_path)
                # print('path_copy1',path_copy)
                path_copy.append(neighbor)
                # print('path_copy2',path_copy)
                qq.enqueue(path_copy)
        

# print(find_ladders('hit', 'cog'))
print(find_ladders('car', 'tie'))