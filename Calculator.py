from tkinter import*
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x1070")
root.title("Calculator By Aditya")
# root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 25 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
f = Frame(root, bg="grey")
b = Button(f, text="C", padx=18, pady=8, font="lucida 22 bold")
b.pack(side=LEFT, padx=4, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="()", padx=18, pady=8, font="lucida 22 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=18, pady=8, font="lucida 22 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=18, pady=8, font="lucida 22 bold")
b.pack(side=LEFT, padx=4, pady=2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
# b.bind("", click)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=4, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=18, pady=8, font="lucida 25 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=18, pady=8, font="lucida 23 bold")
b.pack(side=LEFT, padx=4, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=18, pady=8, font="lucida 23 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=18, pady=8, font="lucida 23 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=18, pady=8, font="lucid 23 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0", padx=18, pady=8, font="lucida 23 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=18, pady=8, font="lucida 22 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=18, pady=8, font="lucida 23 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=18, pady=8, font="lucida 22 bold", bg="blue")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

f.pack()
root.mainloop()

