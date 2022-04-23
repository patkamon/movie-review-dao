from tkinter import *
from tkinter import ttk

import models

list =[]
list = models.session.query(models.Movie)
m = list[0]


def click():
    entered_text= textEntry.get()
    list = []
    for m in models.session.query(models.Movie):
        if m.title.find(entered_text) != -1:
            list.append(m.title)

    list = sorted(list,key=len)
    try:
        m  = models.session.query(models.Movie).filter_by(title=list[0]).first()
        title.set(f'{m.title} |')
        genre.set(f'{m.genre} |')
        lead_studio.set(f'{m.lead_studio} |')
        profit.set(f'{m.profit} |')
        gross.set(f'{m.ww_gross} |')
        year.set(m.year)


    except:
        pass
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


title = StringVar()
title.set(f'{m.title} |')

genre = StringVar()
genre.set(f'{m.genre} |')

lead_studio = StringVar()
lead_studio.set(f'{m.lead_studio} |')

profit = StringVar()
profit.set(f'{m.profit} |')

gross = StringVar()
gross.set(f'{m.ww_gross} |')

year = StringVar()
year.set(m.year)

ttk.Label(frm, textvariable=title).grid(column=1, row=1)
ttk.Label(frm, textvariable=genre).grid(column=2, row=1)
ttk.Label(frm, textvariable=lead_studio).grid(column=3, row=1)
ttk.Label(frm, textvariable=profit).grid(column=4, row=1)
ttk.Label(frm, textvariable=gross).grid(column=5, row=1)
ttk.Label(frm, textvariable=year).grid(column=6, row=1)

textEntry = Entry(window, width = 20)
textEntry.grid(column=0,row= 20)

ttk.Button(window, text='submit', width=6,command=click).grid(column=0,row=21)

output= Text(window, width =75 ,height =6, wrap=WORD,background='cyan' )
output.grid(column=0,row=22)


window.mainloop()
