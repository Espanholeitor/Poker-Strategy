import tkinter as tk
from tkinter import ttk
from play_procedures import *

root = tk.Tk()
root.title("Poker Strategy")
root.geometry("550x600")
root.resizable(False, False)


# Hand Chooser Widget
tk.Label(
    root,
    text="Choose your Hand:",
).grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
Hand = ttk.Combobox(
    root,
    values=["Big Pairs (AA/KK)", "Ace King AK", "Queens QQ", "Small Pairs (JJ to 22)", "Small Connecting Cards",
            "Borderline Hands", "Trash Hands"],
    state="readonly",
)
Hand.grid(row=1, column=0, padx=0, pady=0, sticky=tk.W)

# Submit button Widget
submit = ttk.Button(
    root,
    text="Submit",
    command = lambda:Take_input()
)
submit.grid(row=1, column=0, padx=145, pady=0, sticky=tk.W)

# Text with Hand sugested game Widget
T = tk.Text(root, height = 34, width = 64)
T.grid(row=3, column=0, columnspan=2, padx=0, pady=0, sticky=tk.W)


# Set the results
def Take_input():
    if Hand.get() == "Big Pairs (AA/KK)":
       Tip = Big_Pairs
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "Ace King AK":
       Tip = AK
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "Queens QQ":
       Tip = QQ
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "Small Pairs (JJ to 22)":
       Tip = JJ_to_22
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "Small Connecting Cards":
       Tip = SCC
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "Borderline Hands":
       Tip = BH
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "Trash Hands":
       Tip = TH
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
       



root.mainloop()
