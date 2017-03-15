""" Linked List """

class Node:
    def __init__(self, k):
        self.prev = None
        self.next = None
        self.key = k

class LinkedList:
    def __init__(self):
        self.head = None
        
def list_search(L,k):
    x = L.head
    while x != None and x.key != k:
        x = x.next
    return x

def list_insert(L,x):
    x.next = L.head
    if L.head != None:
        L.head.prev = x
    L.head = x
    x.prev = None

L = LinkedList()
list_insert(L,Node(10))
list_insert(L,Node(1))
result = list_search(L,10)
print(result.key)
result = list_search(L,2)
print(result)
