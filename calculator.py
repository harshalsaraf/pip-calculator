from tkinter import *

root = Tk()
root.title("calculator")

e = Entry(root,width=35, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=15, pady=15)

def calculations(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def calculationsclear():
    e.delete(0, END)

def calculationsadd():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def calculationsequal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "square":
        e.insert(0, f_num * f_num)


def calculationsdivide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



def calculationsmultiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def calculationssubtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

def calculationssquare():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = int(first_number)
    e.delete(0, END)




b1 = Button(root, text="1", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(1))
b2 = Button(root, text="2", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(2))
b3 = Button(root, text="3", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(3))
b4 = Button(root, text="4", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(4))
b5 = Button(root, text="5", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(5))
b6 = Button(root, text="6", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(6))
b7 = Button(root, text="7", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(7))
b8 = Button(root, text="8", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(8))
b9 = Button(root, text="9", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(9))
b0 = Button(root, text="0", padx=40, pady=20, bg="black", fg="white", font=10, command=lambda: calculations(0))
b_add = Button(root, text="+", padx=38, pady=20, font=10, command=calculationsadd)
b_equal = Button(root, text="=", padx=39, pady=20, font=10, command=calculationsequal)
b_subtract = Button(root, text="-", padx=42, pady=20, font=10, command=calculationssubtract)
b_clear = Button(root, text="clear", padx=27, pady=20, font=10, command=calculationsclear)
b_divide = Button(root, text="/", padx=41, pady=20, font=10, command=calculationsdivide)
b_multiply = Button(root, text="x", padx=40, pady=20, font=10, command=calculationsmultiply)
b_square = Button(root, text="square", padx=20, pady=20, font=10, command=calculationssquare)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0, columnspan=1)
b_equal.grid(row=4, column=1)
b_subtract.grid(row=5, column=1)
b_add.grid(row=5, column=0)
b_clear.grid(row=4, column=2, columnspan=1)
b_divide.grid(row=6, column=0)
b_multiply.grid(row=6, column=1)
b_square.grid(row=5, column=2)

root.mainloop()
