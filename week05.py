from unittest import result


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
    
    def search_proc(self, node, val):
        if node == None:
            return False
        if node.data == val:
            return True
        else:
            return self.search_proc(node.next, val)
        return True
    
    def search(self, val):
        result = self.search_proc(self.head, val)
        print(self.search_proc(self.head, val)) # ture false
        return result
        
    def delete_proc(self, node, val):
        if node == None:
            return node
        elif node.data == val:
            tmp = node
            node = node.next
            tmp = None
        elif node.next == None:
            return node
        elif node.next.data == val:
            tmp = node.next
            node.next = node.next.next
            tmp = None
        else:
            node.next = self.delete_proc(node.next, val)
        return node
        
    def delete(self, val):
        if self.search(val):
            # found
            self.head = self.delete_proc(self.head, val)
        else:
            print('not found')
                
    def insertAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
e1 = Node('A')
e2 = Node('B')
e3 = Node('C')

Slink = SlinkedList()
# Slink.head = Slink.insertAtEnd_proc(Slink.head, 'A')
Slink.insertAtEnd('A')
Slink.insertAtEnd('B')
Slink.insertAtEnd('C')
print(Slink.head.data)
# Slink.printList(Slink.head)
# Slink.delete('C')
# Slink.printList(Slink.head)
# Slink.delete('A')
# Slink.printList(Slink.head)
# Slink.insertAtHead('E')
# Slink.printList(Slink.head)
# # Slink.search('E')
# Slink.search('A')
# Slink.search('B')
# Slink.search('C')
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