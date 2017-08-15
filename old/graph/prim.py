
from priorityqueue0 import *
import sys

class vertex:
    def __init__(self, j, key):
        self.j = j
        self.key = key
        self.color = 'white'
        self.adj = []
        
def Comp(x, y):
    return x.key < y.key

nv = 7
ne = 9
e = ["0 1 3","0 2 1","1 2 1","1 3 3","2 3 1","2 4 5","2 5 1","3 4 6","4 5 2"]


V = [vertex(i, sys.maxint) for i in range(nv)]
for i in range(ne):
    x = e[i].split()   
    v1 = int(x[0])
    v2 = int(x[1])
    w = int(x[2])
    V[v1].adj.append([v2, w])
    V[v2].adj.append([v1, w])


pq = Priority_Queue(Comp)
V[0].color = 'grey'
V[0].key = 0
pq.insert(V[0])
Sum = 0
while pq.empty() == False:
    u = pq.extractMin()
    for x in u.adj:
        v = x[0]
        w = x[1]
        if V[v].color == 'white':
            pq.insert(V[v])
            V[v].color = 'grey'
        if V[v].color != 'black':
            if V[v].key > w:
                pq.decreaseKey(V[v], w)

    Sum += u.key
    u.color = 'black'

print Sum


