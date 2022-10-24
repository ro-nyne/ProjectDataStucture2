from asyncio import events
from cProfile import label
from cgitb import text
from ctypes.wintypes import LPWIN32_FIND_DATAA
from operator import truediv
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import os
from ProjectDataStucture2.CanUse import Menu


menu = Menu()


## Def ALL Thing
def page_showall():
    label_tree.delete(1.0, END)
    for i in menu.show_all_data(menu.dlist):
        label_tree.insert(END, str(i) + '\n')

def add():
    addContactWin()

def delete():
    removeContactWin()

def enter():
    en_inAndDel.delete(0, END)
    data = en_inAndDel.get()
    if(menu.search_bool(data)):
        textValue = str(menu.search_in_listnode(data))
        label_tree.delete(1.0, END)
        label_tree.insert(END, textValue)
    else:
        label_tree.delete(1.0, END)
        label_tree.insert(END, "Does not match in Phone Book.")

def exit():
    window.quit()


def addContactWin():
    master = Tk()
    master.title("Add Contact Record.")
    def addContact():
        if(e1.index(END) == 0 or e2.index(END) == 0 or e3.index(END) == 0 or e4.index(END) == 0 or e4.index(END) == 0):
            messagebox.showerror('Warning!', 'Please enter infomation.')
        else:
            if(menu.is_num_check(e4.get()) and len(str(e4.get())) == 10):
                res = messagebox.askquestion('Warning', 'Are you sure?')
                if res == 'yes':
                    menu.enter_contact_record(str(e1.get()), str(e2.get()), e3.get(), e4.get(), e5.get())
                    messagebox.showinfo('Response', 'Add contact successful.')
                    master.destroy()
                elif res == 'no':
                    messagebox.showwarning('error', 'Something went wrong!')
            else:
                messagebox.showwarning('Waring!', 'Phone number is not number or number is less than reality.')
 
    # this will create a label widget
    l1 = Label(master, text = "First name:")
    l2 = Label(master, text = "Last name:")
    l3 = Label(master, text = "Adress:")
    l4 = Label(master, text = "Phone number:")
    l5 = Label(master, text = "E-mail Adress:")
    
    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2.grid(row = 1, column = 0, sticky = W, pady = 2)
    l3.grid(row = 2, column = 0, sticky = W, pady = 2)
    l4.grid(row = 3, column = 0, sticky = W, pady = 2)
    l5.grid(row = 4, column = 0, sticky = W, pady = 2)
    
    # entry widgets, used to take entry from user
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    
    # this will arrange entry widgets
    e1.grid(row = 0, column = 1, pady = 2)
    e2.grid(row = 1, column = 1, pady = 2)
    e3.grid(row = 2, column = 1, pady = 2)
    e4.grid(row = 3, column = 1, pady = 2)
    e5.grid(row = 4, column = 1, pady = 2)
    
    # button widget
    b1 = Button(master, text = "Add Contact", cursor="hand2", command=addContact)
    b1.grid(row = 5, column = 1, sticky = W)
    
    # infinite loop which can be terminated by keyboard
    # or mouse interrupt
    mainloop()

def removeContactWin():
    master = Tk()
    master.title("Remove Contact Record.")
    def removeContact():
        if(e1.index(END) == 0):
            messagebox.showerror('Warning!', 'Please enter infomation.')
        else:
            if(menu.search_bool(e1.get())):
                res = messagebox.askquestion('Warning', 'Are you sure?')
                if res == 'yes':
                    menu.remove_contact(e1.get())
                    messagebox.showinfo('Response', 'Remove contact successful.')
                    master.destroy()
                elif res == 'no':
                    messagebox.showwarning('error', 'OK')
            else:
                messagebox.showwarning('Waring!', 'Does not match in Phone Book.')
 
    # this will create a label widget
    l1 = Label(master, text = "First name:")
    
    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    
    # entry widgets, used to take entry from user
    e1 = Entry(master)
    
    # this will arrange entry widgets
    e1.grid(row = 0, column = 1, pady = 2)
    
    # button widget
    b1 = Button(master, text = "Remove Contact", cursor="hand2", command=removeContact)
    b1.grid(row = 5, column = 1, sticky = W)
    
    # infinite loop which can be terminated by keyboard
    # or mouse interrupt
    mainloop()

window = tk.Tk()
bg = PhotoImage(file='BG.png')
bg_label = tk.Label(window,image=bg)
bg_label.pack()



## Button
bg_btpage1 = PhotoImage(file="enter.png")
bt_page1 = tk.Button(window,image=bg_btpage1,bg="#FFFFFF",activebackground="#FFFFFF",borderwidth=0,cursor="hand2",command=enter)
bt_page1.place(x=447,y=422)

bg_btpage2 = PhotoImage(file="show.png")
bt_page2 = tk.Button(window,image=bg_btpage2,bg="#002f64",activebackground="#002f64",borderwidth=0,cursor="hand2",command=page_showall)
bt_page2.place(x=52,y=500)

bg_btpage3 = PhotoImage(file="add.png")
bt_page3 = tk.Button(window,image=bg_btpage3,bg="#002f64",activebackground="#002f64",borderwidth=0,cursor="hand2",command=add)
bt_page3.place(x=182,y=502)

bg_btpage4 = PhotoImage(file="delete.png")
bt_page4 = tk.Button(window,image=bg_btpage4,bg="#002f64",activebackground="#002f64",borderwidth=0,cursor="hand2",command=delete)
bt_page4.place(x=312,y=502)

bg_btpage5 = PhotoImage(file="exit.png")
bt_page5 = tk.Button(window,image=bg_btpage5,bg="#002f64",activebackground="#002f64",borderwidth=0,cursor="hand2",command=exit)
bt_page5.place(x=442,y=502)

## Entry
inAndDel = StringVar()
en_inAndDel = tk.Entry(window,textvariable=inAndDel,font="supermarket 18",fg="black",bg="#FFFFFF",borderwidth=0)
en_inAndDel.place(x=80,y=430,width=350)

## Show display
scorebarry = Scrollbar(window,orient=VERTICAL)
label_tree = tk.Text(window,yscrollcommand=scorebarry.set,bg="black",bd=0,fg="white",font="supermarket 16")
label_tree.place(x=85, y=180, width=428, height=207)


window.bind("<Return>")
window.resizable(False, False)
window.geometry("600x692")
window.mainloop()