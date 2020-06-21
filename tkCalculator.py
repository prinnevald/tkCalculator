from tkinter import *
import math

# defing the memory of operations and number

class Memory(object):
    def __init__(self):
        self.memory = 0
        self.action = None

### MAIN ###

def main():

    # creating a window

    root = Tk()
    root.title("tkCalculator")

    # field for the text to go

    field = Entry(root, font="Calibri 20", width=30, borderwidth=5)
    field.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
    
    # memory allocation
    
    m = Memory()
    
    # functions for buttons

    def num(number):
        field.insert(END, number)
        
    def add(mem):
        mem.action = "add"
        mem.memory = float(field.get())
        field.delete(0, END)
        
    def sub(mem):
        mem.action = "sub"
        mem.memory = float(field.get())
        field.delete(0, END)
    
    def mul(mem):
        mem.action = "mul"
        mem.memory = float(field.get())
        field.delete(0, END)
    
    def div(mem):
        mem.action = "div"
        mem.memory = float(field.get())
        field.delete(0, END)
        
    def sqr(mem):
        temp = float(field.get())
        field.delete(0, END)
        field.insert(0, math.sqrt(temp))
        
    def dot():
        field.insert(END, ".")
    
    def equal(mem):
        num = float(field.get())
        field.delete(0, END)

        if mem.action == "add":
            field.insert(0, mem.memory + num)
        elif mem.action == "sub":
            field.insert(0, mem.memory - num)
        elif mem.action == "mul":
            field.insert(0, mem.memory * num)
        elif mem.action == "div":
            field.insert(0, mem.memory / num)
        else:
            field.insert(0, "ERROR! Clear and try again.")
    
    def clear(mem):
        mem.memory = 0
        mem.action = None
        field.delete(0, END)

    # creating buttons numbers

    b_1 = Button(root, text="1", padx=40, pady=20, command=lambda:num(1))
    b_2 = Button(root, text="2", padx=40, pady=20, command=lambda:num(2))
    b_3 = Button(root, text="3", padx=40, pady=20, command=lambda:num(3))

    b_4 = Button(root, text="4", padx=40, pady=20, command=lambda:num(4))
    b_5 = Button(root, text="5", padx=40, pady=20, command=lambda:num(5))
    b_6 = Button(root, text="6", padx=40, pady=20, command=lambda:num(6))

    b_7 = Button(root, text="7", padx=40, pady=20, command=lambda:num(7))
    b_8 = Button(root, text="8", padx=40, pady=20, command=lambda:num(8))
    b_9 = Button(root, text="9", padx=40, pady=20, command=lambda:num(9))

    b_0 = Button(root, text="0", padx=89, pady=20, command=lambda:num(0))

    # operations

    b_add = Button(root, text="+", padx=39, pady=20, command=lambda:add(m))
    b_sub = Button(root, text="-", padx=40, pady=20, command=lambda:sub(m))
    b_mul = Button(root, text="*", padx=39, pady=20, command=lambda:mul(m))
    b_div = Button(root, text="/", padx=39, pady=20, command=lambda:div(m))
    b_sqr = Button(root, text="sqrt", padx=32, pady=20, command=lambda:sqr(m))

    # other actions

    b_dot = Button(root, text=".", padx=41, pady=20, command=dot)
    b_eq = Button(root, text="=", padx=38, pady=51, command=lambda:equal(m))
    b_c = Button(root, text="Clear", padx=29, pady=20, command=lambda:clear(m))

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

    b_0.grid(row=4, column=0, columnspan=2)

    b_add.grid(row=1, column=3)
    b_sub.grid(row=2, column=3)
    b_mul.grid(row=1, column=4)
    b_div.grid(row=2, column=4)
    b_sqr.grid(row=3, column=3)

    b_dot.grid(row=4, column=2)
    b_eq.grid(row=3, column=4, rowspan=2)
    b_c.grid(row=4, column=3)
    
    root.resizable(width=False, height=False)
    root.mainloop()

if __name__ == "__main__":
    main()
