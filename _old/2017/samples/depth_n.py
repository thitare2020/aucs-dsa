# Depth of tree in O(n)
import random

counter = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


size = 10
T = Node(int(random.random() * size))
T.left = Node(int(random.random() * size))
T.right = Node(int(random.random() * size))
