from tkinter import Tk, Frame, Label, Button, messagebox
import think
import think1
import form
window = Tk()
window.geometry('500x500')
window.title("Swear Analysis")

label_0 = Label(window, bg="blue", text="SWEAR ANALYSIS",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

button = Button(window, text="Verbal",
                            command=think1.function).place(x=220,y=100)



button2 = Button(window, text="Quantitative",
                            command=think.function).place(x=200,y=140)

b = Button(window, text="Student Information Form",
                            command=form.function).place(x=170,y=180)





