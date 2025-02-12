import tkinter as tk 
from tkinter import messagebox
from main import MathCore as M 
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
        self.entry_var = tk.StringVar()
        self.entry =tk.Entry(root, textvariable=self.entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15)
        
        self.create_buttons()
        
    def create_buttons(self):
        #Create calculator buttons and layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('√', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('DEL', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('ln', 5, 4),
            ('asin', 6, 0), ('acos', 6, 1), ('atan', 6, 2), ('(', 6, 3), (')', 6, 4),
            ('pi', 7, 0), ('%', 7, 1), ('Exit', 7, 2)
            ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 14), bd=5, width=6, height=2,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        #Handles all button click events
        if button_text == "C":
            self.expression = ""
        elif button_text == "DEL":
            self.expression = self.expression[:-1]
        elif button_text == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
        elif button_text in ["sin", "cos", "tan", "asin", "acos", "atan", "Log", "ln" "sqrt", "pi"]:
            
                