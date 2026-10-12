from tkinter import *

def summa():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    lbl.config(text="Сумма: " + str(a + b + c))

def umn():
    print("ok")

root = Tk()
root.title("Калькулятор")
root.geometry("400x300")

Label(root, text="Введите 3 числа и нажмите на кнопку для вычисления суммы").pack(pady=10)

e1 = Entry(root)
e1.pack()
e2 = Entry(root)
e2.pack()
e3 = Entry(root)
e3.pack()

Button(root, text="Сложить", command=summa).pack(pady=10)
Button(root, text="Умножить", command=umn).pack()

lbl = Label(root, text="")
lbl.pack(pady=15)

root.mainloop()
