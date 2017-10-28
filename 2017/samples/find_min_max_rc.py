# Find min and max with no loop

import random
size = 200
counter = 0

A = [int(random.random() * size) for x in range(size)]

min = A[0]
max = A[0]
print(A)


def find_min_max(A):
    global min, max, counter
    counter += 1
    if len(A) == 0:
        return

    if A[0] < min:
        min = A[0]
    if A[0] > max:
        max = A[0]

    A.pop(0)

    find_min_max(A)


find_min_max(A[1:])
print(min, max)
print(counter)
