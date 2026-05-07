from tkinter import *
from random import randint





#define costs of the pizza and toppings
costSmall = 7.50
costMedium = 10.00
costLarge = 15.00
costCheese = 1.00
costPepperoni = 1.50
costMushrooms = 1.25
costPizza = 0.00
costTotal = 0.00
MNTax = float(0.06875)


def Close():
    frmOrder.destroy()

def Reset():
    entCustName.delete(0, END)
    lblCustCopy["text"] = ""
    entCustName.focus()
    Size.set("")
    for topping, toppingSelected, chkTopping in lstValues:
        chkTopping.deselect()
    lstPaymentMethod.selection_clear(0, END)
    lblSizeCost["text"] = "Size Cost: $0.00"
    lblToppingsCost["text"] = "Toppings Cost: $0.00"
    lblCostTotal["text"] = "Total: $0.00"
def Process():
    costToppings = 0.00
    costSize = 0.00
    strCustName = entCustName.get()
    lblCustCopy["text"] = strCustName
    lblOrderNumber["text"] = f"Order Number: {randint(1000, 2000)}"
    if Size.get() == "small":
        costSize = costSmall
    elif Size.get() == "medium":
        costSize = costMedium
    elif Size.get() == "large":
        costSize = costLarge
    else:
        costSize = 0.00
    for topping, toppingSelected, chkTopping in lstValues:
        if toppingSelected.get() == True:
            if topping == "Cheese":
                costToppings += costCheese
            elif topping == "Pepperoni":
                costToppings += costPepperoni
            elif topping == "Mushrooms":
                costToppings += costMushrooms
    costTotal = float((costSize+ costToppings) * (1 + MNTax))
    lblCostTotal["text"] = f"Total: ${costTotal:.2f}"
    lblSizeCost["text"] = f"Size Cost: ${costSize:.2f}"
    lblToppingsCost["text"] = f"Toppings Cost: ${costToppings:.2f}"





# can use the pack, place, or grid geometry manager
# pack is the simplest, but not the most flexible
# place is the most flexible and also simple so we will use this. Dont forget to place the widget on the form.

frmOrder = Tk()
frmOrder.configure(width=2560, height=1440, bg="sky blue")


Size=StringVar()

#Radio Button Creation

radSizeSmall=Radiobutton(variable=Size, text="Small", value="small", fg="navy", bg="sky blue", font="Arial 12")
radSizeSmall.place(x=20, y=280)
radSizeMedium=Radiobutton(variable=Size, text="Medium", value="medium", fg="navy", bg="sky blue", font="Arial 12")
radSizeMedium.place(x=20, y=330)
radSizeLarge=Radiobutton(variable=Size, text="Large", value="large", fg="navy", bg="sky blue", font="Arial 12")
radSizeLarge.place(x=20, y=380)
#set the default value of the size to small using the varible=Size
Size.set("small")

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
lblSizeCost = Label(text='Size Cost: $0.00', font="Arial 12", bg="sky blue", fg="navy")
lblSizeCost.place(x=600, y=400)
lblToppings = Label(text='Toppings', font="Arial 12", bg="sky blue", fg="navy")
lblToppings.place(x=300, y=220)
lblToppingsCost = Label(text='Toppings Cost: $0.00', font="Arial 12", bg="sky blue", fg="navy")
lblToppingsCost.place(x=600, y=440)
lblOrderNumber = Label(text='Order Number', font="Arial 12", bg="sky blue", fg="navy")
lblOrderNumber.place(x=1150, y=180)
lblPaymentMethod = Label(text='Payment Method', font="Arial 12", bg="sky blue", fg="navy")
lblPaymentMethod.place(x=1150, y=220)
lblMNTax = Label(text="MN Sales Tax:6.875 ", font="Arial 12", bg="sky blue", fg="navy")
lblMNTax.place(x=600, y=480)
lblCostTotal = Label(text="Total: $0.00", font="Arial 12", bg="sky blue", fg="navy")

lblCostTotal.place(x=600, y=520)


#Payment Method List Box
lstPaymentMethod = Listbox(font="Arial 12", bg="white", fg="navy")
lstPaymentMethod.place(x=1150, y=280)
lstPaymentMethod.insert(END, "Cash")
lstPaymentMethod.selection_set(0) #cash set as default.
lstPaymentMethod.insert(END, "Credit Card")
lstPaymentMethod.insert(END, "Mobile Pay")
lstPaymentMethod.insert(END, "Crypto")

lstToppings = ["Cheese", "Pepperoni", "Mushrooms"]
lstValues = []
yCounter = 280
for topping in lstToppings:
    toppingSelected = BooleanVar()
    chkTopping = Checkbutton(text=topping, font="Arial 12", bg="sky blue", fg="navy", variable=toppingSelected)
    chkTopping.place(x=300, y=yCounter)
    lstValues.append((topping, toppingSelected, chkTopping))
    yCounter += 50


#Form Creation
frmOrder.title("Not For The Weak Pizzas")
btnReset = Button(text="Reset", font="Arial 12", bg="navy", fg="white", width=8, command=Reset)
btnClose = Button(text="Close", font="Arial 12", bg="navy", fg="white", width=8, command=Close)
btnReset.place(x=650, y=600)
btnClose.place(x=850, y=600)
btnProcess= Button(text="Process Order", font="Arial 12", bg="navy", fg="white", width=15, command=Process)
btnProcess.place(x=300, y=600)
entCustName.focus()
#code that processes the totals of pizzas size, toppings, and tax.


#Main Loop
frmOrder.mainloop()
