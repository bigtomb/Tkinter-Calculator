from calc import Calc
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator ")
root.resizable(0, 0)
frm = ttk.Frame(root, padding=10)
frm.grid()

entry = Entry(frm, font=('arial', 18, 'bold'), width=28, bg="#eee", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipady=10)


calc = Calc(entry)
"""Calculator buttons"""

# First Row
equals_button = Button(frm, text="C", width=38, height=3, cursor="hand2",
                       command=lambda: calc.clear())
equals_button.grid(column=0, row=1, padx=1, pady=1, columnspan=3)

point = Button(frm, text="/", width=10, height=3, cursor="hand2",
               command=lambda: calc.divide())
point.grid(column=3, row=1, padx=1, pady=1)

# Second Row
seven = Button(frm, text="7", width=10, height=3, cursor="hand2",
               command=lambda: calc.click("7"))
seven.grid(column=0, row=2, padx=1, pady=1)

eight = Button(frm, text="8", width=10, height=3, cursor="hand2",
               command=lambda: calc.click("8"))
eight.grid(column=1, row=2, padx=1, pady=1)

nine = Button(frm, text="9", width=10, height=3, cursor="hand2",
              command=lambda: calc.click("9"))
nine.grid(column=2, row=2, padx=1, pady=1)

add_button = Button(frm, text="+", width=10, height=3, cursor="hand2",
                    command=lambda: calc.add())
add_button.grid(column=3, row=2, padx=1, pady=1)

# Third Row
four = Button(frm, text="4", width=10, height=3, cursor="hand2",
              command=lambda: calc.click("4"))
four.grid(column=0, row=3, padx=1, pady=1)

five = Button(frm, text="5", width=10, height=3, cursor="hand2",
              command=lambda: calc.click("5"))
five.grid(column=1, row=3, padx=1, pady=1)

six = Button(frm, text="6", width=10, height=3, cursor="hand2",
             command=lambda: calc.click("6"))
six.grid(column=2, row=3, padx=1, pady=1)

subtract_button = Button(frm, text="-", width=10, height=3, cursor="hand2",
                         command=lambda: calc.subtract())
subtract_button.grid(column=3, row=3, padx=1, pady=1)

# Fourth Row
one = Button(frm, text="1", width=10, height=3, cursor="hand2",
             command=lambda: calc.click("1"))
one.grid(column=0, row=4, padx=1, pady=1)

two = Button(frm, text="2", width=10, height=3, cursor="hand2",
             command=lambda: calc.click("2"))
two.grid(column=1, row=4, padx=1, pady=1)

three = Button(frm, text="3", width=10, height=3, cursor="hand2",
               command=lambda: calc.click("3"))
three.grid(column=2, row=4, padx=1, pady=1)

multiply_button = Button(frm, text="x", width=10, height=3, cursor="hand2",
                         command=lambda: calc.multiply())
multiply_button.grid(column=3, row=4, padx=1, pady=1)

# Fifth Row
zero = Button(frm, text="0", width=25, height=3, cursor="hand2",
              command=lambda: calc.click("0"))
zero.grid(column=0, columnspan=2, row=5, padx=1, pady=1)

equals_button = Button(frm, text="=", width=10, height=3, cursor="hand2",
                       command=lambda: calc.equals())
equals_button.grid(column=3, row=5, padx=1, pady=1)

point = Button(frm, text=".", width=10, height=3, cursor="hand2",
               command=lambda: calc.click("."))
point.grid(column=2, row=5, padx=1, pady=1)

root.mainloop()
