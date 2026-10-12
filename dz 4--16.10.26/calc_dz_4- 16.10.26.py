from tkinter import *

t = 2

def set_t():
    global t
    try:
        t = int(e1.get())
    except ValueError:
        print("Ошибка")

def draw(event):
    c.create_line(event.x, event.y, event.x+1, event.y+1, fill="red", width=t)

root = Tk()
root.title("Графический редактор")
root.geometry("600x450")

c = Canvas(root, bg="white")
c.pack(fill=BOTH, expand=True)
c.bind('<B1-Motion>', draw)

f = Frame(root)
f.pack(side=BOTTOM)

Label(f, text="Толщина:").pack(side=LEFT)
e1 = Entry(f, width=5)
e1.pack(side=LEFT)
Button(f, text="OK", command=set_t).pack(side=LEFT)

root.mainloop()
