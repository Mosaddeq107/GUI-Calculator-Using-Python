from tkinter import*
import math
root=Tk()
#root.iconbitmap('C:/Users/tanji/OneDrive/Desktop/visual code editor/New folder/cal.ico')
root.title("Tanjib's Calculator")
e=Entry(root, width=60, borderwidth=3, bg='gray')
e.grid(row=0, column=0, columnspan=4)

def enter(number):
    l1=e.get()
    e.delete(0, END)
    x=str(l1)+str( number)
    e.insert(0, x)

def clean():
    e.delete(0, END)

def add():
    global first 
    global sign 
    sign='addition'
    first=e.get()
    e.delete(0, END)
def sub():
    global first 
    global sign 
    sign='subtraction'
    first=e.get()
    e.delete(0, END)
def mul():
    global first 
    global sign 
    sign='multiplication'
    first=e.get()
    e.delete(0, END)
def div():
    global first 
    global sign 
    sign='division'
    first=e.get()
    e.delete(0, END)
def sqr_root():
    first=float(e.get())
    b=math.sqrt(first)
    e.delete(0, END)
    e.insert(0, b)
def square():
    first=float(e.get())
    b=first*first
    e.delete(0, END)
    e.insert(0, b)
def percent():
    first=float(e.get())
    b=first*100
    e.delete(0, END)
    e.insert(0, b)
def frac():
    first=float(e.get())
    b=1/first
    e.delete(0, END)
    e.insert(0, b)
def plusmin():
    first=float(e.get())
    b=(first*(-1))
    e.delete(0, END)
    e.insert(0, float(b))


def equal():
    if sign=='addition':
        last=float(e.get())
        e.delete(0, END)
        e.insert(0, float(first)+last)
    elif sign=='subtraction':
        last=float(e.get())
        e.delete(0, END)
        e.insert(0, float(first)-last)
    elif sign=='multiplication':
        last=float(e.get())
        e.delete(0, END)
        e.insert(0, float(first)*last)
    elif sign=='division':
        last=float(e.get())
        e.delete(0, END)
        e.insert(0, float(first)/last)

    


#creating buttons
b1=Button(root, text='7', padx=40, pady=20, command=lambda: enter(7))
b2=Button(root, text='8', padx=40, pady=20, command=lambda: enter(8))
b3=Button(root, text='9', padx=40, pady=20, command=lambda: enter(9))
b4=Button(root, text='√', padx=45, pady=20, command=sqr_root)

b5=Button(root, text='4', padx=40, pady=20, command=lambda: enter(4))
b6=Button(root, text='5', padx=40, pady=20, command=lambda: enter(5))
b7=Button(root, text='6', padx=40, pady=20, command=lambda: enter(6))
b8=Button(root, text='%', padx=45, pady=20, command=percent)

b9=Button(root, text='1', padx=40, pady=20, command=lambda: enter(1))
b10=Button(root, text='2', padx=40, pady=20, command=lambda: enter(2))
b11=Button(root, text='3', padx=40, pady=20, command=lambda: enter(3))
b12=Button(root, text='x^2', padx=40, pady=20, command=square)

b13=Button(root, text='0', padx=40, pady=20, command=lambda: enter(0))
b14=Button(root, text='+', padx=39, pady=20, command=add)
b15=Button(root, text='-', padx=41, pady=20, command=sub)
b16=Button(root, text='1/x', padx=42, pady=20, command=frac)

b17=Button(root, text='.', padx=41, pady=20, command=lambda: enter('.'))
b18=Button(root, text='/', padx=41, pady=20, command=div)
b19=Button(root, text='=', padx=96, pady=20, command=equal)

b20=Button(root, text='+/-', padx=33, pady=20, command=plusmin)
b21=Button(root, text='x', padx=40, pady=20, command=mul)
b22=Button(root, text='Clear', padx=87, pady=20, command=clean)

#showing buttons
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=1, column=3)

b5.grid(row=2, column=0)
b6.grid(row=2, column=1)
b7.grid(row=2, column=2)
b8.grid(row=2, column=3)

b9.grid(row=3, column=0)
b10.grid(row=3, column=1)
b11.grid(row=3, column=2)
b12.grid(row=3, column=3)

b13.grid(row=4, column=0)
b14.grid(row=4, column=1)
b15.grid(row=4, column=2)
b16.grid(row=4, column=3)

b17.grid(row=5, column=0)
b18.grid(row=5, column=1)
b19.grid(row=5, column=2, columnspan=2)

b20.grid(row=6, column=0)
b21.grid(row=6, column=1)
b22.grid(row=6, column=2, columnspan=2)


root.mainloop()


