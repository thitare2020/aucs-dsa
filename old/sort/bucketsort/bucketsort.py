import random
import time

n = input()
a = []
for i in range(n):
    a.append(random.randint(0,n-1))
    a[i] = a[i]/float(n)

d = a[:]

def merge(a,p,q,r):
    
    b = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
    a[p:r+1] = b+a[i:q+1]+a[j:r+1]

def mergesort(a,p,r):
    if p < r:
        q = (p+r)/2
        mergesort(a,p,q)
        mergesort(a,q+1,r)
        merge(a,p,q,r)


def InsertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def bucketsort(a):
    global n

    B = [[] for i in range(n)]
    for i in range(n):
        B[int(n*a[i])].append(a[i])

    for i in range(n):
        InsertionSort(B[i])

    c = []  
    for i in range(n):
        for j in range(len(B[i])):
            c.append(B[i][j])
    return c

time.clock()
a = bucketsort(a)
t1 = time.clock()
print t1
mergesort(d, 0, n-1)
print time.clock()-t1

