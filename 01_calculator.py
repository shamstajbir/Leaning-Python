import tkinter as tk
from math import sqrt


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")

        self.input = []
        self.result = 0
        self.operator = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), justify='right', bd=10)
        self.display.grid(row=0, column=0, columnspan=4)

        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "+", "=",
            "C", "←", "mod", "sqrt"
        ]

        for i, label in enumerate(button_labels):
            button = tk.Button(self, text=label, font=("Arial", 24), command=lambda l=label: self.on_button_click(l))
            button.grid(row=(i // 4) + 1, column=i % 4, sticky="nsew")

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, label):
        try:
            if label == "C":
                self.input.clear()
                self.display.delete(0, tk.END)
                self.result = 0
                self.operator = ""
            elif label == "←":
                if self.input:
                    self.input.pop()
                    self.display.delete(len(self.display.get()) - 1, tk.END)
            elif label == "=":
                if self.input and self.operator:
                    self.result = self.calculate(self.result, float("".join(self.input)), self.operator)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(self.result))
                    self.input.clear()
                    self.operator = ""
            elif label == "sqrt":
                if self.input:
                    self.result = sqrt(float("".join(self.input)))
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(self.result))
                    self.input.clear()
            elif label in ["+", "-", "*", "/", "mod"]:
                if self.input:
                    self.result = float("".join(self.input))
                    self.operator = label
                    self.input.clear()
            else:
                self.input.append(label)
                self.display.insert(tk.END, label)
        except Exception as ex:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.input.clear()
            self.operator = ""

    def calculate(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ArithmeticError("Cannot divide by zero")
            return a / b
        elif operator == "mod":
            return a % b
        else:
            raise ArithmeticError("Unknown operator")


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
