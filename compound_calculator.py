from tkinter import *
def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0,END)
    compound_field.delete(0,END)
    principal_field.focus_set()

# Function to find compound interest
def calculate_ci():
    principal = int(principal_field.get())
    rate=float(rate_field.get())
    time=int(time_field.get())
    CI=principal*(pow(1+rate/100),time)
    compound_field.insert(0,CI)


    #Driver mode
if __name__ == '__main__':
    root=Tk()
    root.configure(background='light blue')
    root.geometry('300x300')
    root.title('Compound Calculator')
    label1=Label(root,text="Principal Amount(Rs):",fg='red',bg='black')
    label2 = Label(root, text="Rate(%) :", fg='red', bg='black')
    label3 = Label(root, text="Time(years):", fg='red', bg='black')
    label4 = Label(root, text="Amount:", fg='red', bg='black')

    #grid method is used for placing
    #padx is used for x axis
    #oady is used for y axis
    label1.grid(row=1,column=1,padx=10,pady=10)
    label2.grid(row=2,column=1,padx=10,pady=10)
    label3.grid(row=3,column=1,padx=10,pady=10)
    label4.grid(row=4,column=1,padx=10,pady=10)

      # Create an entry box
      # for filling or typing the information
    principal_field=Entry(root)
    rate_field=Entry(root)
    time_field=Entry(root)
    compound_field=Entry(root)
        #grid method using placing
    #the weights at respective positions
    principal_field.grid(row=1,column=2,padx=10,pady=10)
    rate_field.grid(row=2,column=2,padx=10,pady=10)
    time_field.grid(row=3,column=2,padx=10,pady=10)
    compound_field.grid(row=4,column=2,padx=10,pady=10)
    #create a button and attached
    #to calculate the function
    button1=Button(root,text="Submit",bg='green',fg='white',command=calculate_ci)
    button2=Button(root,text="Clear",bg='red',fg='white',command=clear_all)
    button1.grid(row=5,column=1,padx=10,pady=10)
    button2.grid(row=5,column=2,padx=10,pady=10)
    root.mainloop()