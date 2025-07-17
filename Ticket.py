# Import libraries
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("600x500")
root.configure(background="#DF4A44")


# Creating a variables for prices
sc = 40
mv = 75
th = 100

# Creating Tkinter widgets
var = StringVar()

e1 = Entry(root, width=10)
e1.grid(row=0, column=1)

cat = ttk.Combobox(root, textvariable=var, width=10, value=["Soccer", "Movie", "Theater"])
cat.grid(row=3, column=1)

num = ttk.Spinbox(root, from_=0, to=100, state="readonly")
num.grid(row=2, column=1)

l1 = Label(root, text="Cellphone number:")
l1.grid(row=0, column=0, sticky=W)

l2 = Label(root, text="Ticket Category:")
l2.grid(row=4, column=0, sticky=W)

l3 = Label(root, text="Number of tickets:")
l3.grid(row=4, column=0, sticky=W)

ans = Label(root)
ans.grid(row=14, column=0)


#Creating class
class TicketSales:
    """Handles ticket sales calculations."""
    VAT_RATE = 0.14
    PRICES = {
        "Soccer": 40,
        "Movie": 75,
        "Theater": 100
    }

    @classmethod
    def calculate_cost(cls, category: str, quantity: int) -> float:
        """Calculate total cost including VAT."""
        base_price = cls.PRICES.get(category, 0)
        return (base_price * quantity) * (1 + cls.VAT_RATE)
# Creates function for button
    def calc():
# Passes through class
        total = TicketSales.calculate_cost(cat.get(), int(num.get()))

# Decision tree
        if cat.get() == "Soccer":
            scprice = sc * int(num.get()) + (14/100)
            ans.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(num.get()) + "\n" +"Number:"+ str(e1.get()))
        if cat.get() == "Movie":
            mvprice = mv * int(num.get()) + (14/100)
            ans.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(num.get()) + "\n" +"Number:"+ str(e1.get()))
        if cat.get() == "Theater":
            thprice = th * int(num.get()) + (14/100)
            ans.config(text="Price:"+ str(thprice) + "\n" + "tickets:"+str(num.get()) + "\n" +"Number:"+ str(e1.get()))

# function

#Creating button
    btn = Button(root, text="calculate", command=calc, width=20, height=1)
    btn.grid(row=8, column=0)
# Adds widgets


root.mainloop()