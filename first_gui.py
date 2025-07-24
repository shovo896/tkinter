from tkinter import *
root = Tk()
root.title("Hello world")
root.geometry("300x300")
menu=Menu(root)
item=Menu(menu)
item.add_command(label='New')
item.add_cascade(label='File',menu=item)
root.config(menu=menu)




lbl=Label(root,text="I love you Dutee")
lbl.grid()
txt=Entry(root,width=10)
txt.grid(column=0,row=1)
def clicked():
    lbl.configure(text="I love you Dutee")

btn=Button(root,text="Click me",fg="red",command=clicked)
btn.grid(column=1,row=1)
root.mainloop()