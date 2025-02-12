"""
Code test filed
"""
import tkinter as tk
from tkinter import messagebox
from main import MathCore as M

class calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("scientific calculator")
        self.root.geometry("500x700")
        self.expression = ""
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15)
        self.create_buttons()

    def create_buttons(self):
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
        if button_text == "C":
            self.expression = ""
        elif button_text == "DEL":
            self.expression = self.expression[:-1]
        elif button_text == "=":
            try:
                self.expression = str(eval(self.expression, {"M": M}))
                                                                            # eval(expression, global), use eval to execute all math
                                                                            # The dictionary {"M": M} maps the string "M" to the MathCore class (aliased as M).
                                                                            # This allows the expression to use M.sin(6) to call MathCore.sin(6).
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
        elif button_text in ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "sqrt", "pi"]:
            self.expression += f"M.{button_text}("
        elif button_text == "^":
            self.expression += "**"
        elif button_text == "√":
            self.expression += "M.sqrt("
        elif button_text == "pi":
            self.expression += "M.pi()"
        elif button_text == "Exit":
            self.root.quit()
        else:
            self.expression += button_text
        self.entry_var.set(self.expression)
window = tk.Tk()
calculator = calculator(window)
window.mainloop()

