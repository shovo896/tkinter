from tkinter import *
expr=""#Global expression string
def press(key):
    global expr
    expr+=str(key)
    display.set(expr)
def equal():
    global expr
    try:
        result=str(eval(expr))
        display.set(result)
        expr=""
    except:
        display.set("expr")
        expr=""
def clear():
    global expr
    expr=""
    display.set("")
if __name__=="__main__":
    root=Tk()
    root.configure(bg="light green")
    root.title("Calculator")
    root.geometry("300x300")
    display=StringVar()
    entry=Entry(root,textvariable=display)
    entry.grid(columnspan=4,inpadx=70)
    #number button

    btn1 = Button(root, text='1', fg='red', command=lambda: press(1), height=1, width=10)
    btn1.grid(columnspan=4,padx=10)
    btn2 = Button(root, text='2', fg='red', command=lambda: press(2), height=1, width=10)
    btn2.grid(columnspan=4,padx=10)
    btn3 = Button(root, text='3', fg='red', command=lambda: press(3), height=1, width=10)
    btn3.grid(columnspan=4,padx=10)
    btn4 = Button(root, text='4', fg='red', command=lambda: press(4), height=1, width=10)
    btn4.grid(columnspan=4,padx=10)
    btn5 = Button(root, text='5', fg='red', command=lambda: press(5), height=1, width=10)
    btn5.grid(columnspan=4,padx=10)
    btn6 = Button(root, text='6', fg='red', command=lambda: press(5), height=1, width=)
    btn6.grid(columnspan=4,padx=10)

    btn7 = Button(root, text='7', fg='red', command=lambda: press(5), height=1, width=10)
    btn7.grid(columnspan=4,padx=10)
    btn8 = Button(root, text='8', fg='red', command=lambda: press(5), height=1, width=10)
    btn8.grid(columnspan=4,padx=10)

    btn9 = Button(root, text='9', fg='red', command=lambda: press(5), height=1, width=10)
    btn9.grid(columnspan=4,padx=10)

    btn0= Button(root, text='0', fg='black', command=lambda: press(5), height=1, width=10)
    btn0.grid(columnspan=4,padx=10)

#operator buttons
plus=Button(root, text='+', fg='red', command=lambda: press('+'), height=1, width=10)
plus.grid(row=2,column=0)
minus=Button(root,text='-', fg='red', command=lambda: press('-'), height=1, width=10)
minus.grid(row=2,column=1)
mult=Button(root,text='*',fg='red',command=lambda : press('*'),height=1,width=0)
mult.grid(row=3,column=0)
div=Button(root,text='/', fg='red',command=lambda: press('/'),height=1,width=0)
div.grid(row=3,column=1)
#other button
eq=Button(root,text='=',fg='black',command=equal,height=1,width=0)
eq.grid(row=4,column=0)
clr=Button(root,text='Clear',fg='red',command=clear,height=1,width=0)
clr.grid(row=5,column=0)
dot=Button(root,text='.',fg='red',command=lambda:press('.'),height=1,width=0)
root.mainloop()