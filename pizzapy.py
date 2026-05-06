from tkinter import *
from random import randint

costSmall = 7.50
costMedium = 10.00
costLarge = 15.00
costCheese = 1.00
costPepperoni = 1.50
costMushrooms = 1.25
costPizza = 0.00
costToppings = 0.00
MNTax = float(0.06875)

def Close():
    frmOrder.destroy()

def Reset():
    entCustName.delete(0, END)
    lblCustCopy["text"] = ""
    entCustName.focus()
    #lblCost["text"] = ""
    Size.set("")
    chkToppings.deselect()
    chkToppings1.deselect()
    chkToppings2.deselect()
    #lblOrderNumber["text"] = ""
    lstPaymentMethod.selection_clear(0, END)
    #lblMNTax["text"] = "0.000"
def Process():
    strCustName = entCustName.get()
    lblCustCopy["text"] = strCustName
    lblOrderNumber["text"] = f"Order Number: {randint(1000, 9999)}"
    costTotal = int((costPizza + costToppings) * 1.06875)





# can use the pack, place, or grid geometry manager
# pack is the simplest, but not the most flexible
# place is the most flexible and also simple so we will use this. Dont forget to place the widget on the form.

frmOrder = Tk()
frmOrder.configure(width=2560, height=1440, bg="sky blue")


Size=StringVar()

#Radio Button Creation

radSize=Radiobutton(variable=Size, text="Small", value="small", fg="navy", bg="sky blue", font="Arial 12")
radSize.place(x=20, y=280)

radSize=Radiobutton(variable=Size, text="Medium", value="medium", fg="navy", bg="sky blue", font="Arial 12")
radSize.place(x=20, y=330)

radSize=Radiobutton(variable=Size, text="Large", value="large", fg="navy", bg="sky blue", font="Arial 12")
radSize.place(x=20, y=380)

#Entry Box Creation
entCustName = Entry(font="Arial 14", bg="white", fg="navy", width=30)
entCustName.place(x=350, y=140)

#Labels
lblCoName = Label(text="Not For The Weak Pizzas", font="Arial 16 bold", bg="sky blue", fg="navy")
lblCoName.place(x=350,y=10)
lblCustName = Label(text="Customer Name:", font="Arial 12", bg="sky blue", fg="navy")
lblCustName.place(x=100, y=140)
lblCustCopy = Label(text="", font="Arial 12", bg="sky blue", fg="navy")
lblCustCopy.place(x=100, y=180)
lblSize = Label(text="Size", font="Arial 12", bg="sky blue", fg="navy")
lblSize.place(x=20, y=220)
lblToppings = Label(text='Toppings', font="Arial 12", bg="sky blue", fg="navy")
lblToppings.place(x=300, y=220)
lblToppingsCost = Label(text='Toppings Cost: $0.00', font="Arial 12", bg="sky blue", fg="navy")
lblToppingsCost.place(x=300, y=430)
lblOrderNumber = Label(text='Order Number', font="Arial 12", bg="sky blue", fg="navy")
lblOrderNumber.place(x=600, y=280)
lblPaymentMethod = Label(text='Payment Method', font="Arial 12", bg="sky blue", fg="navy")
lblPaymentMethod.place(x=1150, y=220)
lblCost = Label(text="Cost: $0.00", font="Arial 12", bg="sky blue", fg="navy")
lblCost.place(x=600, y=320)
lblMNTax = Label(text="MN Sales Tax:6.875 ", font="Arial 12", bg="sky blue", fg="navy")
lblMNTax.place(x=600, y=360)
costTotal = Label(text=f"Total: $0.00", font="Arial 12", bg="sky blue", fg="navy")
costTotal.place(x=600, y=400)


#Payment Method List Box
lstPaymentMethod = Listbox(font="Arial 12", bg="white", fg="navy")
lstPaymentMethod.place(x=1150, y=280)
lstPaymentMethod.insert(END, "Cash")
lstPaymentMethod.insert(END, "Credit Card")
lstPaymentMethod.insert(END, "Mobile Pay")
lstPaymentMethod.insert(END, "Crypto")


#Check Boxes
chkToppings = Checkbutton(text='Cheese', font="Arial 12", bg="sky blue", fg="navy")
chkToppings.place(x=300, y=280)
chkToppings1 = Checkbutton(text='Pepperoni', font="Arial 12", bg="sky blue", fg="navy")
chkToppings1.place(x=300, y=330)
chkToppings2= Checkbutton(text='Mushrooms', font="Arial 12", bg="sky blue", fg="navy")
chkToppings2.place(x=300, y=380)


#Form Creation
frmOrder.title("Not For The Weak Pizzas")
btnReset = Button(text="Reset", font="Arial 12", bg="navy", fg="white", width=8, command=Reset)
btnClose = Button(text="Close", font="Arial 12", bg="navy", fg="white", width=8, command=Close)
btnReset.place(x=650, y=500)
btnClose.place(x=850, y=500)

btnProcess= Button(text="Process Order", font="Arial 12", bg="navy", fg="white", width=15, command=Process)
btnProcess.place(x=300, y=500)
entCustName.focus()


#Main Loop
frmOrder.mainloop()
