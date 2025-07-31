from tkinter import *
from tkinter.ttk import *
#importing strframe function to retrive systems true
from time import strftime
root=Tk()
root.title('Clock')
def time():
    string=strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)
#This function is used to display time on the label
def time():
    string=strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000,time)
#styling the label widget so that clock will look more attractive
lbl=Label(root,font=('calibri',40,'bold'),background='white',foreground='red')
lbl.pack()
time()
mainloop()