# Generate the input
# Number of vertices
V = int(raw_input())
Adj = []
for i in range(V):
    # the number of reachable vertices, list of vertices
    x = raw_input().split()
    Adj.append([])
    for j in range(int(x[0])):
        Adj[i].append(int(x[j+1]))

# Initialise every vertices to white (using color)
color = ['white' for i in range(V)]
f = [-1 for i in range(V)]  # finished time
d = [-1 for i in range(V)]  # arrival time
p = [-1 for i in range(V)]  # origin nodes
time = 0

def dfs_visit(u):
    global color, d, f, p, time
    
    color[u] = 'grey'
    time += 1
    d[u] = time
    for v in Adj[u]:
        if color[v] == 'white':
            p[v] = u
            dfs_visit(v)
    color[u] = 'black'
    time += 1
    f[u] = time

def dfs():
    for i in range(V):
        if color[i] == 'white':
            dfs_visit(i)

dfs()
print p
print d
print f
