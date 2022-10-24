import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import bgcolor
from webbrowser import BackgroundBrowser

root = Tk()
root.title('We here for You')
root.geometry('900x1000')

def search():
    showinfo(
        title=00000,
        message='1111111'
    )



## Create Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


my_canvas = Canvas(main_frame, width=900, height=1000)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

photo = PhotoImage(file='BG.png')
my_canvas.create_image(0,0,image=photo, anchor=NW)

## Add a scrollbar to the canavs
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

## Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox('all')))

my_label = Label(root)
my_label.grid(row=5, column=5)

search_icon = tk.PhotoImage(file='search.png')
search_button = Button(my_canvas, image=search_icon,command=search,bg="#FFFFFF",border=0)
search_button.pack(padx=60, pady=70)

e = Entry(my_canvas,width=30)
e.pack()


root.mainloop()