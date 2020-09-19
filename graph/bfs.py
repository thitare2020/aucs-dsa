from priority_queue import PriorityQueue


def adj(u):
    global G
    global V
    adj_nodes = []
    for v in range(V):
        e = G[u][v]
        if e != 0:
            adj_nodes.append(v)
    return adj_nodes


class _data():
    # Auxilary class to represent a sattelite data.
    # The priority queue maintains its property based on d value.
    def __init__(self, k, d):
        self.index = 0  # index in PQ
        self.key = k    # node number
        self.d = d      # d value

    def __repr__(self):
        # Print nicely to the console (same as toString() in Java)
        return str(self.index) + ':' + str(self.index)


def _comp(a, b):
    # Callback function for comparing two objects.
    # PQ does not know exactly how to compare two objects
    # because it is a generic class
    return a.d < b.d


def BFS(G, s):
    global d, color, p, V, source
    color = [0] * V  # WHITE = 0, GRAY = 1, BLACK = 2
    d = [float('inf')] * V # path weight
    d[source] = 0
    p = [None] * V # parent

    Q = PriorityQueue(_comp)
    x = _data(source, d[source])
    Q.enqueue(x)

    while not Q.empty():
        print(Q.a)
        x = Q.extractMin()
        u = x.key
        for v in adj(u):
            if color[v] == 0:
                color[v] = 1
                d[v] = d[u] + 1
                p[v] = u
                x = _data(v, d[v])
                Q.enqueue(x)
        color[u] = 2


def print_paths(source):
    if source == 1:
        print(1)
    elif p[source] == None:
        print(f"No path from {1} to {source} exists")
    else:
        print_paths(p[source])
        print(source)




    


# Let r = 0, s = 1, t = 2, and so on

G = [
    #r #s #t #u #v #w #x #y
    [0, 1, 0, 0, 1, 0, 0, 0],#r
    [1, 0, 0, 0, 0, 1, 0, 0],#s
    [0, 0, 0, 1, 0, 1, 1, 0],#t
    [0, 0, 1, 0, 0, 0, 1, 1],#u
    [1, 0, 0, 0, 0, 0, 0, 0],#v
    [0, 1, 1, 0, 0, 0, 1, 0],#w
    [0, 0, 1, 1, 0, 1, 0, 1],#x
    [0, 0, 0, 1, 0, 0, 1, 0]#y
]


# Size of V
V = 8
source = 1



BFS(G, source)

for r in G:
    print(r)

print('ADJ of source:', adj(source))
print('color:', color)
print('d:', d)
print('p:', p)
print_paths(3)
