from tkinter import *
from tkinter import ttk

import models

list =[]

def click():
    entered_text= textEntry.get()
    list = []
    for m in models.session.query(models.Movie):
        if m.title.find(entered_text) != -1:
            list.append(m.title)
    # for index, m in enumerate(list):
    #     ttk.Label(frm, text=m.title).grid(column=1, row=1+index)
    #     ttk.Label(frm, text=m.genre).grid(column=2, row=1+index)
    #     ttk.Label(frm, text=m.lead_studio).grid(column=3, row=1+index)
    #     ttk.Label(frm, text=m.profit).grid(column=4, row=1+index)
    #     ttk.Label(frm, text=m.ww_gross).grid(column=5, row=1+index)
    #     ttk.Label(frm, text=m.year).grid(column=6, row=1+index)
    #     if index >= 9:
    #         break;
    output.delete(0.0,END)
    output.insert(END,", ".join(list))



window = Tk()
window.title("Movie Reviews")

frm = ttk.Frame(window, padding=10)
frm.grid()


ttk.Label(frm, text="Title").grid(column=1, row=0)
ttk.Label(frm, text="Genre").grid(column=2, row=0)
ttk.Label(frm, text="Studio").grid(column=3, row=0)
ttk.Label(frm, text="Profit").grid(column=4, row=0)
ttk.Label(frm, text="Gross").grid(column=5, row=0)
ttk.Label(frm, text="Year").grid(column=6, row=0)

list = models.session.query(models.Movie)


for index, m in enumerate(list):
    ttk.Label(frm, text=m.title).grid(column=1, row=1+index)
    ttk.Label(frm, text=m.genre).grid(column=2, row=1+index)
    ttk.Label(frm, text=m.lead_studio).grid(column=3, row=1+index)
    ttk.Label(frm, text=m.profit).grid(column=4, row=1+index)
    ttk.Label(frm, text=m.ww_gross).grid(column=5, row=1+index)
    ttk.Label(frm, text=m.year).grid(column=6, row=1+index)
    if index >= 9:
        break;

textEntry = Entry(window, width = 20)
textEntry.grid(column=0,row= 20)

ttk.Button(window, text='submit', width=6,command=click).grid(column=0,row=21)

output= Text(window, width =75 ,height =6, wrap=WORD,background='white' )
output.grid(column=0,row=22)


window.mainloop()
