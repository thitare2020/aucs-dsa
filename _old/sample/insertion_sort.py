data = [4, 3, 1, 5, 2]

def InsertionSort(A):
  for j in range(1,len(A)):
    key = A[j]
    # insert A[j] into ....
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i+1] = A[i]
      i = i - 1
    A[i+1] = key

print("Insertion Sort")
x = range(1,len(data))
print(list(x))
print("Input",data)
InsertionSort(data)
print("Output",data)
