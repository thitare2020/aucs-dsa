class PriorityQueue:
    # def __init__(self, CompareFunc):
    def __init__(self):
        # self.Comp = CompareFunc
        self.a = []

    def empty(self):
        return self.a == []

    def heapify(self, i):
        l = i * 2 + 1
        r = (i + 1) * 2
        # if l < len(self.a) and self.Comp(self.a[i], self.a[l]) == False:
        if l < len(self.a) and self.a[i] < self.a[l]:
            largest = l
        else:
            largest = i
        if r < len(self.a) and self.a[largest] >= self.a[r]:
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            # self.a[i].index = i
            # self.a[i].largest = largest
            self.heapify(largest)

    def enqueue(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        # self.a[i].index = i
        j = int((i - 1) / 2)
        # while i > 0 and self.Comp(self.a[i], self.a[j]) == True:
        while i > 0 and self.a[i] < self.a[j]:
            self.a[i], self.a[j] = self.a[j], self.a[i]
            # self.a[i].index = i
            # self.a[j].index = j
            i = j
            j = int((i - 1) / 2)

    def extractMin(self):
        x = self.a[0]
        i = len(self.a) - 1
        self.a[0], self.a[i] = self.a[i], self.a[0]
        # self.a[0].index = 0
        # self.a[i].index = i
        del self.a[i]
        self.heapify(0)
        return x


if __name__ == '__main__':
    Q = PriorityQueue()
    Q.enqueue(10)
    Q.enqueue(5)
    Q.enqueue(4)
    Q.enqueue(2)
    Q.enqueue(3)

    print(Q.a)

    Q.enqueue(11)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(1)
    Q.enqueue(9)

    print(Q.a)
