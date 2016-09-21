def find_max(a,i):
    m = 0
    for i in range(1,i+1):
        if a[i] > a[m]:
            m = i
    return m

def selection_sort(a):
    for i in range(len(a)-1,-1,-1):
        j = find_max(a,i)
        a[i],a[j] = a[j],a[i]

A = [9,8,7,6,5,4,3,2,1]

selection_sort(A)

print A
