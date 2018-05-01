# Find 10 largest elements from a list at O(n) time.
import random
size = 100
A = [int(random.random() * size) for x in range(size)]

B = []

counter = 0


def find_max(A):
    global counter
    max = float('-inf')
    j = 0
    for i in range(1, len(A)):
        counter += 1
        if A[i] > max:
            max = A[i]
            j = i
    return A.pop(j)


for i in range(10):
    counter += 1
    B.append(find_max(A))

print(A)
print(B)
print(counter)
