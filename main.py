import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Poker Preflop Strategy")
root.geometry("500x200")
root.resizable(False, False)



# Hand Chooser Widget
tk.Label(
    root,
    text="Choose your Hand:",
).grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
Hand = ttk.Combobox(
    root,
    values=["AA or KK", "AK", "QQ", "JJ to 22"],
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
T = tk.Text(root, height = 9, width = 61)
T.grid(row=3, column=0, columnspan=2, padx=0, pady=0, sticky=tk.W)


# Set the results
def Take_input():
    if Hand.get() == "AA or KK":
       Tip = "Raise"
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)
    elif Hand.get() == "JJ to 22":
       Tip = "Fold"
       T.delete('1.0', tk.END)
       T.insert(tk.END, Tip)





root.mainloop()
