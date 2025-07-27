from tkinter import StringVar

def __init__():
    window = TK()
    window.title("Loan Calculator")
    #window title
    Label(window,text="Annual Interest rate").grid(row=1,column=1,sticky=W)
    Label(window,text="Number of years".grid(row=2,column=1,sticky=W)
    Label(window,text="Loan amount").grid(row=2,column=1,sticky=W)
    Label(window,text="Monthly Payment").grid(row=4,column=1,sticky=W)
    Label(window,text="Total Payment").grid(row=5,column=1,sticky=W)
    # for taking inputs
    self.annualInterestRate = StringVar()
    Entry(window,textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)
    self.numberOfYearsVar = StringVar()
    Entry(window,textvariable=self.numberOfYearsVar,justify=RIGHT).grid(row=2,column=2)

    self.loanAmountVar=StringVar()
    Entry(window,textvariable=self.loanAmountvar,justify=RIGHT).grid(row=3,column=2)

    self.monthlyPaymentVar=StringVar()
    lblMonthlyPayment(window,textvariable=self.monthlyPaymentVar,justify=RIGHT).grid(row=4,column=2,sticky=E)

    self.totalPaymentVar=StringVar()
    iblTotalPayment=Label(window,textvariable=self.totalPaymentVar,justify=RIGHT).grid(row=5,column=2,sticky=E)

    btComputePayment=Button(window,text="Compute Payment",command=self.coputePayment).grid(row=6,column=2,sticky=E)
    window.mainloop()



# adding funtionality
def computePayment(self):
    # compute the total payment
     monthlyPayment=self.getMonthlyPayment(float(self.LoanAmountVar.get()),
                                           float(self.annualInterestRateVar.get())/1200,
                                           int(self.numberOfYearsVar.get()))
     self.monthlyPaymentVar.set(format(monthlyPayment,'10.2f'))
     totalPayment=float(self.monthlyPaymentVar.get()*12\ *int(self.numberOfYearsVar.get())*12\ *int(self.numberOfYerasVar.get())
    self.totalPaymentVar.set(format(totalPayment,'10.2f'))
def getMonthlypayment(self,loanAmount,monthlyInterestRate,numberOfYerars):
     monthlyPayment=loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))
retrun monthlyPayment;




                                           )





                                           )