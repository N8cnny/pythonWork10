#File name: MessageBox.py
import tkinter
from tkinter import *

def Show(str):
 root = Tk()
 root.title('Message Box')
 Label(root, justify=LEFT, text = str).grid(padx= 10, pady=5)

 root.mainloop()
