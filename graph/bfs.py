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


def BFS(G, s):
    global d, color, p, V
    color = [0] * V  # WHITE = 0, GRAY = 1, BLACK = 2
    d = [float('inf')] * V
    d[source] = 0
    p = [None] * V

    Q = PriorityQueue()
    Q.enqueue(source)

    while not Q.empty():
        print(Q.a)
        u = Q.extractMin()
        for v in adj(u):
            if color[v] == 0:
                color[v] = 1
                d[v] = d[u] + 1
                p[v] = u
                Q.enqueue(v)
        color[u] = 2


def print_paths(source):
    pass


# Let r = 0, s = 1, t = 2, and so on
G = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

G = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0]
]

# Size of V
V = 8
source = 1

BFS(G, source)

print(G)
print(adj(0))
print('color:', color)
print('d:', d)
print('p:', p)
