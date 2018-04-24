from disjointsets import DisjointSets


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self):
        return "%d,%d:%d" % (self.u, self.v, self.w)


# Generate the graph from the input
# Number of vertices
V = int(input())
E = int(input())

elist = []
for i in range(E):
    x = input().split()
    u, v, w = int(x[0]), int(x[1]), int(x[2])
    e = Edge(u, v, w)
    elist.append(e)

elist.sort(key=lambda x: x.w)
print(elist)


def kruskal():
    A = []
    ds = DisjointSets(V)  # make set
    for e in elist:
        u = e.u
        v = e.v
        if ds.findset(u) != ds.findset(v):
            A.append(e)
            ds.union(u, v)
    return A


T = kruskal()
print(T)
