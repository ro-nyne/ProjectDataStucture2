from asyncore import read
from Data import Data
from Node import Dlist

file_name = "D:\SouceCode\Python\ProjectDataStucture2\phonebook.txt"

class Menu:
    
    def __init__(self):
        self.file_name = file_name
        file1 = open(self.file_name, "a+")
        file1.close
        self.node = Dlist()
        self.readFile()
        self.show_main_menu()
        
    def removetxt(self, value):
        return ''.join(value.splitlines())
    
    def readFile(self):
        file = open(self.file_name, "r+")
        file_content = file.readlines()
        
        for line in file_content:
            self.node.insertAtEnd(self.removetxt(line))
        # self.node.printList()
        
    def show_main_menu(self):
        self.node.printList()
        ''' Show main menu for Phone Book Program '''
        print("\n   *** Phone Book Menu ***\n"+
            "------------------------------------------\n"+
            "Enter 1 To Display all contact\n" +
            "Enter 2 To Add a New Contact Record\n"+
            "Enter 3 To Search your contacts\n"+
            "Enter 4 To Quit\n**********************")
        choice = input("Enter your choice: ")
        if choice == "1":
            file1 = open(self.file_name, "r+")
            file_contents = file1.read()
            if len(file_contents) == 0:
                print("Phone Book is empty")
            else:
                print (file_contents)
            file1.close
            self.show_main_menu()
        elif choice == "2":
            self.enter_contact_record()
            self.show_main_menu()
        elif choice == "3":
            self.search_contact_record()
            self.show_main_menu()
        elif choice== "4":
            print("Thanks for using Phone Book Program")
        else:
            print("Wrong choice, Please Enter [1 to 4]\n")
            self.show_main_menu()
        
    def search_contact_record(self):
        ''' This function is used to searches a specific contact record '''
        search_name = input("Enter First name for Searching contact record: ")

        search_name = search_name.title()
        file1 = open(self.file_name, "r+")
        file_contents = file1.readlines()
        
        found = False   
        for line in file_contents:
            if search_name in line:
                print("Your Required Contact Record is:", end=" ")
                print (line)
                found=True
                break
        if  found == False:
            print("There's no contact Record in Phone Book with name = " + search_name )

    def enter_contact_record(self):
        ''' It  collects contact info firstname, last name, email and phone '''
    
        first = input('Enter First Name: ')
        first = first.title()
        last = input('Enter Last Name: ')
        last = last.title()
        adrs = input('Enter Adress: ')
        phone = input('Enter Phone number: ')
        email = input('Enter E-mail: ')
        contact = ("[" + first + " " + last + ", " + adrs + ", " + phone + ", " + email +  "]\n")
        self.node.insertAtEnd(Data(first+" "+last, adrs, phone, email))
        file1 = open(self.file_name, "a")
        file1.write(contact)
        
        self.node.insertAtEnd(Data(first+" "+last, adrs, phone, email))
        print( "This contact\n " + contact + "has been added successfully!")
        
m1 = Menu()