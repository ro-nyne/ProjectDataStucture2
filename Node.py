# Collect name, adress, phone number, e-mail
class Node:
    
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
class Dlist:
    
    def __init__(self):
        self.head = None
    
    def insertAtEnd_proc(self, node, val):
        if node == None:
            newNode = Node(val)
            node = newNode
        elif node.next == None:
            newNode = Node(val)
            node.next = newNode
            newNode.prev = node
        else:
            node.next = self.insertAtEnd_proc(node.next, val)
        
        return node

    def insertAtEnd(self, val):
        self.head = self.insertAtEnd_proc(self.head, val)
        
    def printList_proc(self, node):
        if node == None:
            print('None')
        else:
            print(str(node.data) + ' <-> ', end='')
            self.printList_proc(node.next)
         
    def printListRev_proc(self, node): # reverse list
        if node == None:
            print('None', end='')
        else:
            self.printListRev_proc(node.next)
            print(' <-> ' + str(node.data), end='')
    
    def printList(self):
        self.printList_proc(self.head)
        # self.printListRev_proc(self.Head)
        