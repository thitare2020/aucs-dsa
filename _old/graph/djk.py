from priority_queue import PriorityQueue

V = int(input())
s = int(input())
w = [[]] * V
for i in range(V):
    l = [int(x) for x in input().split()]
    w[i] = l


class Vertex:
    def __init__(self, i):
        self.i = i
        self.p = None
        self.d = float('inf')

    def __repr__(self):
        return "%d:%s:%s" % (self.i, self.p, self.d)


def adj(ui):
    global w, V
    alist = []
    for i in range(V):
        if w[ui][i] > 0:
            alist.append(i)
    return alist


def comp(x, y):
    return x.d < y.d


def relax(u, v):
    global w
    if v.d > u.d + w[u.i][v.i]:
        v.d = u.d + w[u.i][v.i]
        v.p = u.i


def dijkstra():
    global S, s
    S = []
    Q = PriorityQueue(comp)

    vlist = []
    for i in range(V):
        vObj = Vertex(i)
        vlist.append(vObj)
        if i == s:
            vObj.d = 0
        Q.enqueue(vObj)

    while not Q.empty():
        u = Q.extractMin()
        S.append(u)
        for vi in adj(u.i):
            v = vlist[vi]
            relax(u, v)


S = []
dijkstra()
print(S)
