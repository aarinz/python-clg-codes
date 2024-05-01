from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox

window = Tk()
window.title("Registration form")
window.geometry("500x300")
window.config()

label0= Label(window, text="Registration form", width=20, font=38, fg="Red")
label0.place(x=30, y=10)

label1 = Label(window, text="Full name", width=10)
label1.place(x=10, y=45)
entry1 = Entry(window, width=50)
entry1.place(x=90, y=45)

label2 = Label(window, text="Email ", width=10, font=("bold", 10))
label2.place(x=0, y=90)
entry2 = Entry(window, width=50)
entry2.place(x=90, y=90)

label3 = Label(window, text="Gender", width=10, font=("bold", 10))
label3.place(x=0, y=135)
var = IntVar() #for selection of one circle
Radiobutton(window, text="Male", padx=10, variable=var, value=1).place(x=80, y=135)
Radiobutton(window, text="Female", padx=10, variable=var, value=2).place(x=138, y=135)

label4 = Label(window, text="Country", width=10, font=("bold", 10))
label4.place(x=2, y=175)
str = StringVar() #string dropdown
country = ttk.Combobox(window, width=25, textvariable=str, state="readonly")
country['values'] = ("select your country", "afghan", "india", "china")
country.set("select your country")
country.place(x=90, y=180)

label5 = Label(window, text="Programming", width=10, font=("bold", 10))
label5.place(x=15, y=220)
var1 = IntVar()
Checkbutton(window, text="Java", padx=5, variable=var1).place(x=100, y=220)
var2 = IntVar()
Checkbutton(window, text="Python", padx=10, variable=var2).place(x=150, y=220)

def success():
    messagebox.showinfo(title="form", message="Your Registration form is created successfully")

b = Button(window, text="Submit", width=10, bg="red", fg="white", command=success)
b.place(x=10, y=270)

window.mainloop()