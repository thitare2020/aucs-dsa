

class nilnode:
    def __init__(self):
        self.color = 'black'
        self.l = self
        self.r = self
        self.p = self
        
class node:
    def __init__(self, key):
        global NilT
        
        self.k = key
        self.color = 'red'
        self.l = NilT
        self.r = NilT
        self.p = NilT

def L_rotate(x): # x.r must not be None
    global T, NilT
    y = x.p
    z = x.r
    x.r = z.l
    z.l = x
    x.p = z
    if y == NilT:  # x was the root
        T = z
        z.p = NilT
    else:
        if y.l == x:
            y.l = z
            z.p = y
        else:
            y.r = z
            z.p = y

def R_rotate(x): # x.l must not be None
    global T, NilT
    y = x.p
    z = x.l
    x.l = z.r
    z.r = x
    x.p = z
    if y == NilT:  # x was the root
        T = z
        z.p = NilT
    else:
        if y.l == x:
            y.l = z
            z.p = y
        else:
            y.r = z
            z.p = y

def paint(x,color): # x must not be NilT
    x.color = color

def inorder_tree_walk(x):
    global NilT, T
    
    if x != NilT:
        inorder_tree_walk(x.l)
        if x == T:
            print str(x.k)+'*'
        else:
            print x.k
        inorder_tree_walk(x.r)

def tree_search(x,k):
    global NilT
    
    if x == NilT or k == x.k:
        return x
    if k < x.k:
        return tree_search(x.l,k)
    else:
        return tree_search(x.r,k)
    
def minimum(x):
    while x.l != NilT:
        x = x.l
    return x

def maximum(x):
    while x.r != NilT:
        x = x.r
    return x

def successor(x):
    if x.r != NilT:
        return minimum(x.r)
    y = x.p
    while y != NilT and x == y.r:
        x = y
        y = y.p
    return y

def insert(z):
    global NilT, T
    
    y = NilT
    x = T
    while x != NilT:
        y = x
        if z.k < x.k:
            x = x.l
        else:
            x = x.r
    z.p = y
    if y == NilT:   # empty tree
        T = z
    elif z.k < y.k:
        y.l = z
    else:
        y.r = z
        
def case(x):
    global NilT
    
    if x.l == NilT and x.r == NilT:
        return 1
    if x.l != NilT or x.r != NilT:
        c = 2
    if x.l != NilT and x.r != NilT:
        c = 3
    return c

def delete(x):
    global NilT, T
    
    c = case(x)
    if c == 3:
        z = successor(x)
        c = case(z)
        x.k, z.k = z.k, x.k
    else:
        z = x
        
    if c == 1:
        y = z.p
        if y == NilT:   # z is root
            T = NilT
        else:
            if z == y.l:
                y.l = NilT
            else:
                y.r = NilT

    if c == 2:
        y = z.p
        if z.l != NilT:
            w = z.l
        else:
            w = z.r
            
        if y == NilT:    # z is root
            T = w
            w.p = NilT
        else:
            if y.l == z:
                y.l = w
            else:
                y.r = w
            w.p = y
            
    return z


def rbInsert(x):
    global T, NilT
    insert(x)
    x.color = 'red'
    # Fix-up code follows here
        
        

NilT = nilnode()

T = NilT

a = node(20)
rbInsert(a)
a = node(30)
rbInsert(a)
a = node(10)
rbInsert(a)
a = node(25)
rbInsert(a)
a = node(28)
rbInsert(a)

inorder_tree_walk(T)
