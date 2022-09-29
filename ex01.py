from hashlib import new
from traceback import print_last


class Node:
    def  __init__(self, data = None):
        self.data = data
        self.next = None
        
class SlinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self, node):
        if node == None:
            print('None')
        else:
            print(node.data + ' -> ', end='')
            self.printList(node.next)
            
    def printListLoop(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data + ' -> ', end='')
            ptr = ptr.next
        print('None')
        
    def insertAtEnd_proc(self, node, val):
        if node == None:
            # insert here
            newNode = Node(val)
            node = newNode
        else:
            node.next = self.insertAtEnd_proc(node.next, val)
        return node
    
    def insertAtEnd(self, val):
        self.head = self.insertAtEnd_proc(self.head, val)
    
    
e1 = Node('A')
e2 = Node('B')
e3 = Node('C')

Slink = SlinkedList()
# Slink.head = Slink.insertAtEnd_proc(Slink.head, 'A')
Slink.insertAtEnd('A')
Slink.insertAtEnd('B')
Slink.insertAtEnd('C')
Slink.printList(Slink.head)
# Slink.head = e1
# Slink.head.next = e2
# Slink.head.next.next = e3
# Slink.printListLoop()
# print(Slink.head.data)

# e1.next = e2
# e1.next.next = e3
# print(Slink.head.next.data)

# print(e1.data)
# print(e2.data)
# print(e1.data, e1.next.data, e1.next.next.data)