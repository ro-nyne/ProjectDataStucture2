from Data import Data
from Node import Dlist

class Menu:
    
    def __init__(self):
        self.file_name = "D:\SouceCode\Python\ProjectDataStucture2\phonebook.txt"
        file1 = open(self.file_name, "a+")
        file1.close
        self.node = Dlist()
        self.show_main_menu()
        
    def show_main_menu(self):
        ''' Show main menu for Phone Book Program '''
        print("\n   *** Phone Book Menu ***\n"+
            "------------------------------------------\n"+
            "Enter 1 To Display Your Contacts Records\n" +
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
            ent = input("Press Enter to continue ...")
            self.show_main_menu()
        elif choice == "2":
            self.enter_contact_record(self.node)
            ent = input("Press Enter to continue ...")
            self.show_main_menu()
        elif choice == "3":
            self.search_contact_record()
            ent = input("Press Enter to continue ...")
            self.show_main_menu()
        elif choice== "4":
            print("Thanks for using Phone Book Program")
        else:
            print("Wrong choice, Please Enter [1 to 4]\n")
            ent = input("Press Enter to continue ...")
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

    def enter_contact_record(self, node):
        ''' It  collects contact info firstname, last name, email and phone '''
    
        first = input('Enter First Name: ')
        first = first.title()
        last = input('Enter Last Name: ')
        last = last.title()
        adrs = input('Enter Adress: ')
        phone = input('Enter Phone number: ')
        email = input('Enter E-mail: ')
        contact = ("[" + first + " " + last + ", " + adrs + ", " + phone + ", " + email +  "]\n")
        file1 = open(self.file_name, "a")
        file1.write(contact)
        
        self.node.insertAtEnd(Data(first+" "+last, adrs, phone, email))
        self.node.printList()
        print( "This contact\n " + contact + "has been added successfully!")
        
Menu()