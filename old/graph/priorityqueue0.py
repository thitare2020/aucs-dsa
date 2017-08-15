
# Each obj to be inserted must be a class instance
# A field called 'index' will be added

class Priority_Queue:
    def __init__(self, CompareFunc):
        self.Comp = CompareFunc
        self.a = []
        
    def empty(self):
        if self.a == []:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < len(self.a) and self.Comp(self.a[i], self.a[l]) == False:
            largest = l
        else:
            largest = i
        if r < len(self.a) and self.Comp(self.a[largest], self.a[r]) == False:
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.a[i].index = i
            self.a[i].largest = largest
            self.heapify(largest)
        
    def insert(self, x):
        self.a.append(x)
        i = len(self.a)-1
        self.a[i].index = i
        j = (i-1)/2
        while i > 0 and self.Comp(self.a[i], self.a[j]) == True:
            self.a[i],self.a[j] = self.a[j],self.a[i]
            self.a[i].index = i
            self.a[j].index = j
            i = j
            j = (i-1)/2

    def extractMin(self):
        x = self.a[0]
        i = len(self.a)-1
        self.a[0],self.a[i] = self.a[i],self.a[0]
        self.a[0].index = 0
        self.a[i].index = i
        del self.a[i]
        self.heapify(0)
        return x

    def decreaseKey(self, x, k):
        x.key = k
        i = x.index
        j = (i-1)/2
        while i > 0 and self.Comp(self.a[i], self.a[j]) == True:
            self.a[i],self.a[j] = self.a[j],self.a[i]
            self.a[i].index = i
            self.a[j].index = j
            i = j
            j = (i-1)/2

#class MyClass:
#    def __init__(self, k):
#        self.key = k

#def Comp(x,y):
#    return x.key < y.key

#l = []
#for i in range(10):
#    l.append(MyClass(100-i))

#pq = Priority_Queue(Comp)
#for x in l:
#    pq.insert(x)
