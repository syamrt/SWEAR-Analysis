from tkinter import *
import graph
global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10
def function(name,verbal,quantitative,academics,goal):
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10
    master = Tk() 
    Label(master, text='Name: '+name).grid(row=0)
    Label(master, text='Strength in Verbal(%): '+str(verbal)).grid(row=1)
    Label(master, text='Strength in Quantitative(%): '+str(quantitative)).grid(row=2)
    Label(master, text='Strength in Academics(%): '+str(academics)).grid(row=3)
    Label(master, text='Your Goal: '+goal).grid(row=4)
    Label(master, text='All the Best!!!').grid(row=5)
    graph.plotg(academics,verbal,quantitative)
    mainloop()



