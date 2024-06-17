import tkinter as tk
import random


root = tk.Tk()
root.title("Propose Yes or No")
root.geometry("300x200")

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

def propose():
    responses = [
        "Yes, but only if you do the dishes!",
        "No, but you can try again later.",
        "Absolutely, but you owe me a pizza!",
        "No way, José!",
        "Yes, but don't tell anyone!",
        "No, I need more coffee first.",
        "Yes, but only if you sing a song!",
        "No, my cat doesn't approve."
    ]
    result = random.choice(responses)
    result_label.config(text=result)


propose_button = tk.Button(root, text="Propose", command=propose, font=("Helvetica", 14))
propose_button.pack(pady=20)

root.mainloop()
