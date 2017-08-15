heap_size = 0

def parent(i):
    return int(i/2)

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def max_heapify(A,i):
    global heap_size
    l = left(i)
    r = right(i)
    #print heap_size,i,l,r
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,largest)

def build_max_heap(A):
    global heap_size
    heap_size = len(A)
    #print range(int(len(A)/2)-1,-1,-1)
    for i in range(int(len(A)/2)-1,-1,-1):
        max_heapify(A,i)
        
def heapsort(A):
    global heap_size
    build_max_heap(A)
    #print range(len(A)-1,0,-1)
    for i in range(len(A)-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heap_size -= 1
        max_heapify(A,0)
        #print A
