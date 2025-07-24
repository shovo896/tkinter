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
    btn2 = Button(root, text='2', fg='red', command=lambda: press(2), height=1, width=10)
    btn3 = Button(root, text='3', fg='red', command=lambda: press(3), height=1, width=10)
    btn4 = Button(root, text='4', fg='red', command=lambda: press(4), height=1, width=10)
    btn5 = Button(root, text='5', fg='red', command=lambda: press(5), height=1, width=10)
