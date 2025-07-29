from tkinter import *
def getParcentile():
    students=int(total_participantField.get())
    rank=int(rankField.get())
    result=round((students-rank)/students*100,3)
    # inserting method inserting the
    # value of the text entry box
    participantField.insert(10,str(result))
#Function for clearing the contents of  all text entry boxes
def Clear:
    #deleting the content from all entry box
    rankField.delete(0,END)
    total_participantField.delete(0,END)
    percentileField.delete(0,END)


 #driver code
 if __name__=='__main__':
     gui=Tk()
     gui.configure(background="lightblue")
     gui.title("Rank based -Parcentile Calculator")
     gui.geometry("600x300")
     #Create a rank:label
     rank=Label(gui,text="And",bg='blue')
     #Create a And :Label
     and1=Label(gui,text="And",bg='blue')
     #create a Total participants : Label
     total_participant=Label(gui,text="Total Participant",bg='blue')
#Create a find percentile button attached to getPercentile function

     find=Button(gui,text="Find",bg='blue',command=getParcentile)
     #create a parcentile :Label
     percentile=Label(gui,text="percentile",bg='blue')
     #Create a clear button and attached to clear function
     clear=Button(gui,text="Clear",fg="Black",bg="red",command=clear)
     #grid method is used for placing
     #the widgets at respestive positions
     #in table like structure
     #padx attributed provide x-axis margin
     #from the root window to the winget
     rank.grid(row=1,column=1,padx=18)
     and1.grid(row=2,column=4)
     total_participant.grid(row=3,column=4,padx=10)
     #pady attribute provide y margin from the widget
     find.grid(row=4,column=1,pady=10)
     percentile.grid(row=5,column=1,pady=10)
     clear.grid(row=6,column=1,pady=10)
     #create text entry box for filling or typing an information
     rankField=Entry(gui)
     total_participantField=Entry(gui)
     percentileField=Entry(gui)
     #start the gui
     gui.mainloop()

