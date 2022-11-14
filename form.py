from tkinter import *
import result
import think
import think1
global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e15
def function():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e15
    master = Tk() 
    Label(master, text='First Name').grid(row=0)
    Label(master, text='Last Name:').grid(row=1)
    Label(master, text='Father Name:').grid(row=2)
    Label(master, text='Mother Name:').grid(row=3)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    Label(master, text='Gender:').grid(row=4)
    b=Radiobutton(master,text='MALE',variable='M',value='M')
    b1=Radiobutton(master,text='FEMALE',variable='M',value='F')
    b.grid(row=4, column=1)
    b1.grid(row=4, column=2)
    Label(master, text='Date Of Birth:').grid(row=5)
    e5 = Entry(master)
    e5.grid(row=5, column=1)
    Label(master, text='State:').grid(row=6)
    e6 = Entry(master)
    e6.grid(row=6, column=1)
    Label(master, text='District:').grid(row=7)
    e7 = Entry(master)
    e7.grid(row=7, column=1)
    Label(master, text='Address:').grid(row=8)
    e8 = Entry(master)
    e8.grid(row=8, column=1)
    Label(master, text='Academic Details:').grid(row=9)
    Label(master, text='10th Class(CGPA):').grid(row=10)
    e9 = Entry(master)
    e9.grid(row=10, column=1)
    Label(master, text='Inter-Groups(%):').grid(row=11)
    e10 = Entry(master)
    e10.grid(row=11, column=1)
    Label(master, text='Inter-Language(%):').grid(row=12)
    e11 = Entry(master)
    e11.grid(row=12, column=1)
    Label(master, text='Interests:').grid(row=13)
    e12 = Entry(master)
    e12.grid(row=13, column=1)
    Label(master, text='Strengths:').grid(row=14)
    e13 = Entry(master)
    e13.grid(row=14, column=1)
    Label(master, text='Languages Known:').grid(row=15)
    e14 = Entry(master)
    e14.grid(row=15, column=1)
    Label(master, text='Goal:').grid(row=16)
    e15 = Entry(master)
    e15.grid(row=16, column=1)
    global status
    status=1
    button=Button(master,text='Submit',command=report)
    button.grid(row=17, column=0)
    mainloop()

def hai():
    aca= (int((float(e9.get())*10))+int(e10.get())+int(e11.get()))/3
    
    result.function(e1.get()+' '+e2.get(),think.right*10,think1.right*10,aca,e15.get())


def report():
    if think.status==0 or think1.status==0:
        messagebox.showinfo("Error","Please Attempt both Verbal and Quantitative Quizes")
    else:
        hai()

