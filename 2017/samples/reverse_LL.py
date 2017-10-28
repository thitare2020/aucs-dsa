# Recursive reverse linked list
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


size = 10
H = Node(int(random.random() * size))
T = H
for i in range(size):
    T.next = Node(int(random.random() * size))
    T = T.next


def print_LL(H):
    C = H
    while C != None:
        print(C.data, end=' ')
        C = C.next
    print()


def reverse_LL(C, P):
    N = C.next
    C.next = P

    if N == None:
        return C
    else:
        return reverse_LL(N, C)


print_LL(H)
H = reverse_LL(H, None)
print_LL(H)
