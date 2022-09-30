# Double LinkedList

class Node():
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
class Dlist:
    def __init__(self):
        self.Head = None
        
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
        self.Head = self.insertAtEnd_proc(self.Head, val)
        
    def insertAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.Head
        self.Head.prev = newNode
        self.Head = newNode
    
    def insertAtIndex_proc(self, node, val, index, nowindex = 0):
        if node == None:
            pass
        elif index == nowindex + 1:
            newNode = Node(val)
            newNode.next = node.next
            newNode.prev = node
            node.next.prev = newNode
            node.next = newNode
        else:
            node.next = self.insertAtIndex_proc(node.next, val, index, nowindex+1)
            
        return node
        
    def insertAtIndex(self, val, index):
        self.Head = self.insertAtIndex_proc(self.Head, val, index)
    
    def printList_proc(self, node):
        if node == None:
            print('None')
        else:
            print(node.data + ' <-> ', end='')
            self.printList_proc(node.next)
            
    def printListRev_proc(self, node):
        if node == None:
            print('None', end='')
        else:
            self.printListRev_proc(node.next)
            print(' <-> ' + node.data, end='')
    
    def printList(self):
        self.printList_proc(self.Head)
        # self.printListRev_proc(self.Head)
        
    def search_proc(self, node, val):
        if node == None:
            return False
        elif node.data == val:
            return True
        else:
            return self.search_proc(node.next, val)
    
    def search(self, val):
        self.search_proc(self.Head, val)
        
    def searchIndex_proc(self, node, val, index = -1):
        if node == None:
            return -1
        elif node.data == val:
            return index+1
        else:
            return self.searchIndex_proc(node.next, val, index+1)
    
    def searchIndex(self, val):
        return self.searchIndex_proc(self.Head, val)
    
    def delete_proc(self, node, val):
        if node == None:
            pass
        elif node.data == val:
            if node.next != None and node.prev != None:
                node.next.prev = node.prev
                node.prev.next = node.next
                tmp = node
                node = node.next
                tmp = None
            elif node.next == None and node.prev == None:
                node = None
            elif node.next == None:
                node = None
            elif node.prev == None:
                tmp = node
                node = node.next
                tmp = None
        else:
            node.next = self.delete_proc(node.next, val)
        return node
    
    def delete(self, val):
        if self.searchIndex(val) == -1:
            print('not found')
        else:
            self.Head = self.delete_proc(self.Head, val)
        
d1 = Dlist()
d1.insertAtEnd('A')
d1.insertAtEnd('B')
d1.insertAtEnd('C')
d1.printList()
d1.delete('C')
d1.printList()

d1.insertAtHead('G')
d1.printList()
d1.insertAtIndex('F', 1)
d1.printList()
# print(d1.searchIndex('B'))
# print(d1.searchIndex('A'))
# print(d1.searchIndex('C'))
# print(d1.Head.data)
# print(d1.Head.next.data)
# print(d1.Head.next.prev.data)