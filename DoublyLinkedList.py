# Collect name, adress, phone number, e-mail
from email import header
from os import link


class Node:
    
    def __init__(self, data, prev = None, next = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
        
    def __str__(self) -> str:
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})

    def __repr__(self) -> str:
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})
        
class Dlist:
    
    def __init__(self) -> None:
        '''
        Initializes the head and tail of the linked list to None and initializes the length to zero.
        '''
        self.head: Node = None
        self.tail: Node = None
        self.lenght = 0
        
    def __str__(self) -> str:
        '''
        Returns string representation of the linked list.
        '''
        linkedlist = ''
        
        current = self.head
        
        while current:
            linkedlist += str(current.data)
            linkedlist += ' -> '
            current = current.next
            
        linkedlist += 'None'
        
        return linkedlist
    
    def __repr__(self) -> str:
        return str(self.head)
        
    def insert_at_head(self, data) -> None:
        '''
        Inserts a node at the 0th position or first position in the linked list.
        The newly inserted node becomes the head of the list, and in the event
        that the list was empty the tail was well.
        '''
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail - node
            self.lenght += 1
            return
        
        node = Node(data, next=self.head)
        self.head = node
        self.head.next.prev = self.head
        self.lenght += 1
    
    def insert_at_tail(self, data) -> None:
        '''
        Inserts a node at the last position in the linked list.
        The newly inserted node becomes the tail of the linked list.
        '''
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            self.lenght += 1
            return
        
        node = Node(data, prev = self.tail)
        previous_tail = self.tail
        self.tail.next = node
        self.tail = node
        self.tail.prev = previous_tail
        self.lenght += 1
    
    def insert_at(self, index: int, data) -> None:
        pass
    
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
        
    def printLstRev(self):
        self.printListRev_proc(self.head)
        
    def search_proc(self, node, val):
        if node == None:
            return False
        elif node.data == val:
            return True
        else:
            return self.search_proc(node.next, val)
    
    def search(self, val):
        self.search_proc(self.head, val)
        
    def searchIndex_proc(self, node, val, index = -1):
        if node == None:
            return -1
        elif node.data == val:
            return index+1
        else:
            return self.searchIndex_proc(node.next, val, index+1)
    
    def searchIndex(self, val):
        return self.searchIndex_proc(self.head, val)
    
    def search_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return None
    
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
            self.head = self.delete_proc(self.head, val)