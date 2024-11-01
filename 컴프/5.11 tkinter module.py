
from tkinter import *

window = Tk( )

label1=Label(window, text="Hello World")
label1.pack()
label2=Label(window, text="Hello World", width=20,height=3,fg="blue")
label2.pack()

b1=Button(window, text="버튼1", fg="red")
b2=Button(window, text="버튼2", bg="blue")
b1.pack()
b2.pack()

window.mainloop( )

