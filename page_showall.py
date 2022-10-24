import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import home
from PIL import ImageTk,Image
from tkinter import messagebox
import os

## Def All....
def page_main():
    print("Click Home Button")

window = tk.Tk()
bg = PhotoImage(file='BG2.png')
bg_label = tk.Label(window,image=bg)
bg_label.pack()



## Button
bg_btpage5 = PhotoImage(file="home.png")
bt_page5 = tk.Button(window,image=bg_btpage5,bg="black",activebackground="black",borderwidth=0,cursor="hand2",command=page_main)
bt_page5.place(x=250,y=455)

## Show display
scorebarry = Scrollbar(window,orient=VERTICAL)
label_tree = tk.Text(window,yscrollcommand=scorebarry.set,bg="black",bd=0,fg="white",font="supermarket 16")
label_tree.place(x=85, y=180, width=428, height=207)


window.bind("<Return>")
window.resizable(False, False)
window.geometry("600x692")
window.mainloop()