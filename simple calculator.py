from tkinter import *
root=Tk()
root.title("CALCULATOR")
#creating entry box

e=Entry(root,width=40,borderwidth=4)
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20) 

#put button values

def onclick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(num))

def clear():
    e.delete(0,END)

def add():
    fn=e.get()
    global fnum
    global m
    m="add"
    fnum=int(fn)
    e.delete(0,END)

def sub():
    fn=e.get()
    global fnum
    global m
    m="sub"
    fnum=int(fn)
    e.delete(0,END)

def mul():
    fn=e.get()
    global fnum
    global m
    m="mul"
    fnum=int(fn)
    e.delete(0,END)

def div():
    fn=e.get()
    global fnum
    global m
    m="div"
    fnum=int(fn)
    e.delete(0,END)

def equal():
    sn=e.get()
    e.delete(0,END)
    if m=="add":
        e.insert(0,fnum+int(sn))
    if m=="sub":
        e.insert(0,fnum-int(sn))
    if m=="mul":
        e.insert(0,fnum*int(sn))
    if m=="div":
        e.insert(0,fnum/int(sn))    

#creating buttons

button_1=Button(root, text="1",padx=30,pady=15,command=lambda: onclick(1))
button_2=Button(root, text="2",padx=30,pady=15,command=lambda: onclick(2))
button_3=Button(root, text="3",padx=30,pady=15,command=lambda: onclick(3))
button_4=Button(root, text="4",padx=30,pady=15,command=lambda: onclick(4))
button_5=Button(root, text="5",padx=30,pady=15,command=lambda: onclick(5))
button_6=Button(root, text="6",padx=30,pady=15,command=lambda: onclick(6))
button_7=Button(root, text="7",padx=30,pady=15,command=lambda: onclick(7))
button_8=Button(root, text="8",padx=30,pady=15,command=lambda: onclick(8))
button_9=Button(root, text="9",padx=30,pady=15,command=lambda: onclick(9))
button_0=Button(root, text="0",padx=30,pady=15,command=lambda: onclick(0))
button_equal=Button(root, text="=",padx=30,pady=15,command=equal)
button_clear=Button(root, text="C",padx=30,pady=15,command=clear)
button_add=Button(root,text="+",padx=30,pady=15,command=add)
button_sub=Button(root,text="-",padx=30,pady=15,command=sub)
button_mul=Button(root,text="*",padx=30,pady=15,command=mul)
button_div=Button(root,text="/",padx=30,pady=15,command=div)

#adding buttons to frame
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_add.grid(row=1,column=3)


button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1)
button_clear.grid(row=4,column=2)
button_div.grid(row=4,column=3)


root.mainloop()