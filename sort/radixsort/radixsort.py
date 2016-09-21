def counting_sort(A, j):   # j is power of the digit d-1, ... , 0
    c = [0]*10
    for i in range(len(A)):
        c[(A[i]/(10**j))%10] += 1
    for k in range(1,len(c)):
        c[k] += c[k-1]
    B = [0]*len(A)
    for i in range(len(A)-1, -1, -1):
        B[c[(A[i]/(10**j))%10]-1] = A[i]
        c[(A[i]/(10**j)%10)] -= 1
    A[:] = B[:]

def radixsort(A):
    x = max(A)
    d = 0
    while x != 0:
        d += 1
        x /= 10
    for j in range(d):
        counting_sort(A,j)

    
