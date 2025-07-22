
import tkinter as tk

def button_clicked():
    print("Button Clicked")

root = tk.Tk()

# Creating a button with corrected parameters
button = tk.Button(
    root,
    text="Click me",
    command=button_clicked,
    activebackground="red",
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",  # corrected from "haand2"
    disabledforeground="black",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",  # corrected from "hightlightbacxkground"
    highlightcolor="black",
    highlightthickness=2,
    justify="center",
    overrelief="flat",
    padx=10,
    pady=10,
    width=15,
    wraplength=120
)

button.pack(padx=20, pady=20)
root.mainloop()





