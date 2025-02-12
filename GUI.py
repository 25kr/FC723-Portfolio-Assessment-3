import tkinter as tk 
from tkinter import messagebox
from main import MathCore
class calculator:
    """
    This will be a GUI for a calculator application, 
    once the app is open you'll see the same things as shown in the normal calculator
    """
    def __init__(self, root):
        self.root = root
        self.root.title("scientific calculator")
        self.root.geometry("400x600")
        self.root.resizeable(False, False)
        
        self.expression = ""
        self.entry.var = tk.StringVar()
        self.entry =tk.Entry(root, textvariable=self.entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15)
        
        self.create_buttons()