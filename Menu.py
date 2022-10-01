from platform import node
from unicodedata import name
from Data import Data
from DoublyLinkedList import Dlist, Node

file_name = "D:\SouceCode\Python\ProjectDataStucture2\phonebook.txt"

class Menu:
    
    def __init__(self):
        ''' 
        This function will activate when call this class.
        '''
        self.file_name = file_name
        file1 = open(self.file_name, "a+")
        file1.close
        self.dlist = Dlist()
        self.read_file()
        # self.print_somthing()
        self.show_main_menu()

    def remove_ln(self, value = '\n'):
        '''
        Removes 'new line' from text.
        '''
        return ''.join(value.splitlines())
    
    def read_file(self):
        '''
        Reads file and keep in list.
        '''
        file = open(self.file_name, "r+")
        file_content = file.readlines()
        
        for line in file_content:
            if line != None:
                list = line.split(', ')
                self.dlist.insert_at_tail(Data(list[0], list[1], list[2], self.remove_ln(list[3])))
            else:
                return
    
    def print_somthing(self):
        self.remove_all_contact()
                    
    def show_main_menu(self):
        '''
        Display menu to do somthing.
        '''
        print("\n================= Phone Book Menu =================\n"+
            "\n---------------------------------------------------\n"+
            "\n\tEnter 1 To Display all contact\n" +
            "\tEnter 2 To Add a New Contact\n"+
            "\tEnter 3 To Search your contacts\n"+
            "\tEnter 4 To Quit\n"+
            "\tEnter 5 To Delete all contact\n\n---------------------------------------------------\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            if self.dlist.is_empty():
                print("\nPhone Book is empty\nAdd new contact enter >> 2 <<")
            else:
                self.display_all_node(self.dlist.head)
            self.show_main_menu()
        elif choice == "2":
            self.enter_contact_record()
            self.show_main_menu()
        elif choice == "3":
            self.search_contact()
            self.show_main_menu()
        elif choice== "4":
            print("Thanks for using ....\n")
        elif choice == "5":
            self.remove_all_contact()
            self.show_main_menu()
        else:
            print("Wrong choice, Please Enter [1 to 4]\n")
            self.show_main_menu()
            
    def display_all_node(self, node):
        if node is None:
            return
        else:
            print(node.data)
            self.display_all_node(node.next)
            
    def search_contact(self):
        search_name = input("Enter First name for searching contact record: ")
        search_name = search_name.title()
        val_name = self.search_in_listnode(search_name)
        
        if val_name is None:
            print("There's no contact Record in Phone Book with name = " + search_name)
        else:
            print("Your Required Contact Record is:", end=" ")
            print(val_name)
    
    def search_in_file(self, val: str):
        val = val.title()
        file = open(self.file_name, "r+")
        file_contents = file.readlines()
        
        for line in file_contents:
            if val in line:
                list = line.split(', ')
                return self.remove_ln(list[0])
            
    def search_in_listnode_proc(self, node, val):
        if node is None:
            return None
        else:
            if node.data.name == val:
                return node.data
            elif node.data.name != val:
                return self.search_in_listnode_proc(node.next, val)
            else:
                return None
            
    def search_in_listnode(self, val):
        val = self.search_in_file(val)
        return self.search_in_listnode_proc(self.dlist.head, val)
            
    def enter_contact_record(self):
        '''
        add contact
        '''
        first = input('Enter First Name: ')
        first = first.title()
        last = input('Enter Last Name: ')
        last = last.title()
        adrs = input('Enter Adress: ')
        phone = input('Enter Phone number: ')
        phone = self.is_num_check(phone)
        phone = self.phone_format(phone)
        email = input('Enter E-mail Adress: ')
        
        contact_data = Data(first+" "+last, adrs, phone, email)
        ## Write in text file
        self.dlist.insert_at_tail(repr(contact_data))
        file1 = open(self.file_name, "a")
        file1.write(repr(contact_data)+'\n')
        ## Add to Doubly Likedlist
        self.dlist.insert_at_tail(Data(first+" "+last, adrs, phone, email))
        print( "This contact\n " + str(contact_data) + " ..has been added successfully!")
        
    def is_num_check(self, val):
        '''
        Cheack values is numeric or not.
        '''
        while True:
            if val.isnumeric():
                return val
            else:
                print("That does not contian with number. Please enter again.")
                retype = input('Enter Phone number: ')
                val = self.is_num_check(retype)
                return val

    def remove_contact(self):
        '''
        remove contact
        '''
        search_name = input("Enter First name for remove: ")
        contact_data = self.search_in_listnode(search_name)

        if contact_data != None:
            self.dlist.remove_data(contact_data)
            
    def remove_all_contact(self):
        lenght_node = self.dlist.get_length()
        for i in range(lenght_node):
            self.dlist.remove_at_tail()
            
        file = open(self.file_name, 'w')
        file.seek(0)
        file.write('')
        file.truncate()
        print('Delete all contact successfullt!...')
            
    def edit_contact(self):
        '''
        Edit infonation from old data
        '''
        edit_name = input('Enter First Name you want to Edit: ')
        edit_name = edit_name.title()
        
        contact_data = self.search_in_file(edit_name)
        if contact_data != None:
            contact_data = self.dlist.find(contact_data)
        else:
            print(edit_name +' does not match in Phone book.')
        
    def phone_format(self, val):
        '''
        Format phone number like 98-435-8456
        '''
        return '+' + format(int(val[:-1]), ",").replace(",", "-") + val[-1]


m1 = Menu()