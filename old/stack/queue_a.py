""" Array-based queue """
head  = 0
tail = 0

def enqueue(Q,x):
    global head, tail
    Q[tail] = x
    if tail == len(Q):
        tail = 0
    else:
        tail = tail + 1

def dequeue(Q):
    global head, tail
    x = Q[head]
    if head == len(Q):
        head = 0
    else:
        head = head + 1
    return x

Q = [0 for x in range(10)]
print(dequeue(Q))
