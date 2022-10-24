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
        self.show_main_menu()
    
    def read_file(self):
        '''
        Reads file and store in linked list. If the file is empty will do
        nothng.
        '''
        file = open(self.file_name, "r+")
        file_content = file.readlines()
        
        for line in file_content:
            if line != None:
                list = line.split(', ')
                self.dlist.insert_at_tail(Data(list[0], list[1], list[2], self.remove_ln(list[3])))
            else:
                return
                    
    def show_main_menu(self):
        '''
        Display all menu.
        '''
        print("\n================= Phone Book Menu =================\n"+
            "\n---------------------------------------------------\n"+
            "\n\tEnter 1 To Display all contact\n" +
            "\tEnter 2 To Add a New Contact\n"+
            "\tEnter 3 To Search your contacts\n"+
            "\tEnter 4 To Quit\n"+
            "\tEnter 5 To Delete all contact\n"+
            "\tEnter 6 To Delete contect\n\n---------------------------------------------------\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            if self.dlist.is_empty():
                print("\n\tPhone Book is empty...\n")
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
            print("\nThanks for using.... see you next time.\n")
        elif choice == "5":
            self.remove_all_contact()
            self.show_main_menu()
        elif choice == "6":
            self.remove_contact()
            self.show_main_menu()
        # elif choice == "7":
        #     self.print_somthing()
        #     self.show_main_menu()
        else:
            print("\nWrong choice, Please Enter [1 to 4]\n")
            self.show_main_menu()
            
    def display_all_node(self, node):
        '''
        Display all node
        '''
        if node is None:
            return None
        else:
            print(node.data)
            self.display_all_node(node.next)
#------------------------- Search --------------------------
    def search_contact(self):
        '''
        Search contact by fisrt name.
        '''
        if self.dlist.is_empty() != True:
            search_name = input("Enter First name for searching contact Record: ")
            search_name = search_name.title()
            val_name = self.search_in_listnode(search_name)
            
            if val_name is None:
                print("There's no contact Record in Phone Book with name = " + search_name)
            else:
                print("Your Required Contact Record is:", end=" ")
                print(val_name)
        else:
            print('\nPhone Book is empty now...\n')
    
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
        if self.dlist.is_empty() != True:
            val = self.search_in_file(val)
            return self.search_in_listnode_proc(self.dlist.head, val)
        else:
            print('\nPhone Book is empty now...\n')
#-------------------------------------------------------------  
    def enter_contact_record(self):
        '''
        Adds new contact.
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
        # Write in text file
        file1 = open(self.file_name, "a")
        file1.write(repr(contact_data)+'\n')
        # Add to Doubly Likedlist
        self.dlist.insert_at_tail(contact_data)
        print( "This contact\n-> " + str(contact_data) + " *** has been added successfully!")
        

    def remove_contact(self):
        '''
        Delete one of contacts.
        '''
        if self.dlist.is_empty() != True:
            search_name = input("Enter First name for delete contact Record: ")
            contact_data = self.search_in_listnode(search_name)

            val = search_name.title()
            with open(self.file_name, "r+") as file:
                file_contents = file.readlines()
            for line in file_contents:
                if val in line:
                    file_want_to_replace = line
                
            if contact_data != None:
                self.dlist.remove_data(contact_data)
                self.inplace_change(self.file_name, file_want_to_replace, '')
                print(self.dlist.print_list())
                print('Delete contact Record successfully!...')
            else:
                print('Does not match with contact Record.')
        else:
            print('\nPhone book is empty now...\n')
            
    def remove_all_contact(self):
        '''
        Delete all of contacts.
        '''
        if self.dlist.is_empty() != True:
            lenght_node = self.dlist.get_length()
            for i in range(lenght_node):
                self.dlist.remove_at_tail()
                
            file = open(self.file_name, 'w')
            file.seek(0)
            file.write('')
            file.truncate()
            print('\nDelete all contact successfully!!...\n')
        else:
            print('\nPhone book is empty now...\n')

    def is_num_check(self, val):
        '''
        Cheack values is numeric or not.
        '''
        while True:
            if val.isnumeric():
                return val
            else:
                print("Does not contian with number. Please enter again.")
                retype = input('Enter Phone number: ')
                val = self.is_num_check(retype)
                return val
    
    def inplace_change(self, filename, old_string, new_string):
        '''
        Replace text in file.txt
        '''
        with open(filename) as f:
            s = f.read()
            if old_string not in s:
                print('"{old_string}" not found in {filename}.'.format(**locals()))
                return

        with open(filename, 'w') as f:
            print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
            s = s.replace(old_string, new_string)
            f.write(s)
            
    def phone_format(self, val):
        '''
        Format phone number like 98-435-8456
        '''
        if len(str(val)) <= 1:
            return val
        else:
            return '+' + format(int(val[:-1]), ",").replace(",", "-") + val[-1]
            
    def remove_ln(self, value = '\n'):
        '''
        Removes 'new line' from text.
        '''
        return ''.join(value.splitlines())
    
    # def print_somthing(self):
    #     self.dlist.bubble_sort_node('asc')
    #     self.dlist.print_list()
    #     self.dlist.bubble_sort_node('desc')
    #     self.dlist.print_list()
        
m1 = Menu()