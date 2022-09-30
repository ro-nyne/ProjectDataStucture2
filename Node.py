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