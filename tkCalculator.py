from tkinter import *
from tkinter import ttk

# main function

def main():

    # creating a window

    root = Tk()
    root.title("tkCalculator")

    # field for the text to go

    field = Entry(root, width=35, borderwidth=5)
    field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # function for buttons

    def but_c(number):
        field.delete(0, END)
        field.insert(0, number)

    # creating buttons

    b_1 = Button(root, text="1", padx=40, pady=20, command=lambda:but_с(1))
    b_2 = Button(root, text="2", padx=40, pady=20, command=lambda:but_с(2))
    b_3 = Button(root, text="3", padx=40, pady=20, command=lambda:but_с(3))

    b_4 = Button(root, text="4", padx=40, pady=20, command=lambda:but_с(4))
    b_5 = Button(root, text="5", padx=40, pady=20, command=lambda:but_с(5))
    b_6 = Button(root, text="6", padx=40, pady=20, command=lambda:but_с(6))

    b_7 = Button(root, text="7", padx=40, pady=20, command=lambda:but_с(7))
    b_8 = Button(root, text="8", padx=40, pady=20, command=lambda:but_с(8))
    b_9 = Button(root, text="9", padx=40, pady=20, command=lambda:but_с(9))

    b_0 = Button(root, text="0", padx=40, pady=20, command=lambda:but_с(0))

    b_add = Button(root, text="+", padx=39, pady=20, command=lambda:but_с())
    b_eq = Button(root, text="=", padx=91, pady=20, command=lambda:but_с())
    b_c = Button(root, text="Clear", padx=79, pady=20, command=lambda:but_с())

    # arranging buttons in the window

    b_1.grid(row=3, column=0)
    b_2.grid(row=3, column=1)
    b_3.grid(row=3, column=2)

    b_4.grid(row=2, column=0)
    b_5.grid(row=2, column=1)
    b_6.grid(row=2, column=2)

    b_7.grid(row=1, column=0)
    b_8.grid(row=1, column=1)
    b_9.grid(row=1, column=2)

    b_0.grid(row=4, column=0)

    b_add.grid(row=5, column=0)
    b_c.grid(row=4, column=1, columnspan=2)
    b_eq.grid(row=5, column=1, columnspan=2)
    
    root.mainloop()


if __name__ == "__main__":
    main()
