from tkinter import *
from tkinter import ttk

import service
import models


def fetch_from_search():
    # get title for search from textEntry
    search_title= textEntry.get().lower()
    list = service.get_movie_titles_from_title(search_title)

    # sort them from shorten length first
    list = sorted(list,key=len)

    # set result from search to cyan area
    output.delete(0.0,END)
    output.insert(END,", ".join(list))

    try:
        return service.get_movie_from_title(list[0]), service.get_review_from_title(list[0])
    except:
        pass

def update():
    m,r = fetch_from_search()
    m.title = title_entry.get()
    m.genre = genre_entry.get()
    m.lead_studio = studio_entry.get()
    m.profit = profit_entry.get()
    m.ww_gross = gross_entry.get()
    m.year = year_entry.get()
    r.audience_score = a_entry.get()
    r.rt_score = rt_entry.get()
    service.models.session.commit()
    # to update all input and output
    search()



def set_search_ui(m,r):
    title.set(f'{m.title} |')
    genre.set(f'{m.genre} |')
    lead_studio.set(f'{m.lead_studio} |')
    profit.set(f'{m.profit} |')
    gross.set(f'{m.ww_gross} |')
    year.set(f'{m.year} |')
    audience_score.set(r.audience_score)
    rt_score.set(r.rt_score)

def set_update_ui(m,r):
    title_entry.delete(0,END)
    genre_entry.delete(0,END)
    studio_entry.delete(0,END)
    profit_entry.delete(0,END)
    gross_entry.delete(0,END)
    year_entry.delete(0,END)
    a_entry.delete(0,END)
    rt_entry.delete(0,END)

    title_entry.insert(0,m.title)
    genre_entry.insert(0,m.genre)
    studio_entry.insert(0,m.lead_studio)
    profit_entry.insert(0,m.profit)
    gross_entry.insert(0,m.ww_gross)
    year_entry.insert(0,m.year)
    a_entry.insert(0,r.audience_score)
    rt_entry.insert(0,r.rt_score)

def search():
    movie,review = fetch_from_search()
    set_search_ui(movie,review)
    set_update_ui(movie,review)



# fetch start
list = service.get_movie_titles_from_title("")
movie = service.get_movie_from_title(list[0])
review = service.get_review_from_title(list[0])

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
ttk.Label(frm, text="Audience review(%)").grid(column=7, row=0)
ttk.Label(frm, text="Rotten Tomatoes review(%)").grid(column=8, row=0)

# MOVIE
title = StringVar()
genre = StringVar()
lead_studio = StringVar()
profit = StringVar()
gross = StringVar()
year = StringVar()
# REVIEW
audience_score = StringVar()
rt_score = StringVar()


title.set(f'{movie.title} |')
genre.set(f'{movie.genre} |')
lead_studio.set(f'{movie.lead_studio} |')
profit.set(f'{movie.profit} |')
gross.set(f'{movie.ww_gross} |')
year.set(f'{movie.year} |')
audience_score.set(review.audience_score)
rt_score.set(review.rt_score)

ttk.Label(frm, textvariable=title).grid(column=1, row=1)
ttk.Label(frm, textvariable=genre).grid(column=2, row=1)
ttk.Label(frm, textvariable=lead_studio).grid(column=3, row=1)
ttk.Label(frm, textvariable=profit).grid(column=4, row=1)
ttk.Label(frm, textvariable=gross).grid(column=5, row=1)
ttk.Label(frm, textvariable=year).grid(column=6, row=1)
ttk.Label(frm, textvariable=audience_score).grid(column=7, row=1)
ttk.Label(frm, textvariable=rt_score).grid(column=8, row=1)

textEntry = Entry(window, width = 20)
textEntry.grid(column=0,row= 20)

ttk.Button(window, text='search title', width=12,command=search).grid(column=0,row=21)

output= Text(window, width =75 ,height =6, wrap=WORD,background='cyan' )
output.grid(column=0,row=22)


frm2 = ttk.Frame(window, padding=10)
frm2.grid()

title_entry = Entry(frm2, width =20)
title_entry.grid(column=1,row= 23)
genre_entry = Entry(frm2, width = 8)
genre_entry.grid(column=2,row= 23)
studio_entry = Entry(frm2, width = 16)
studio_entry.grid(column=3,row= 23)
profit_entry = Entry(frm2, width = 6)
profit_entry.grid(column=4,row= 23)
gross_entry = Entry(frm2, width = 6)
gross_entry.grid(column=5,row= 23)
year_entry = Entry(frm2, width = 4)
year_entry.grid(column=6,row= 23)
a_entry = Entry(frm2, width = 4)
a_entry.grid(column=7,row= 23)
rt_entry = Entry(frm2, width = 4)
rt_entry.grid(column=8,row= 23)


title_entry.insert(0,movie.title)
genre_entry.insert(0,movie.genre)
studio_entry.insert(0,movie.lead_studio)
profit_entry.insert(0,movie.profit)
gross_entry.insert(0,movie.ww_gross)
year_entry.insert(0,movie.year)
a_entry.insert(0,review.audience_score)
rt_entry.insert(0,review.rt_score)

ttk.Button(window, text='update', width=8,command=update).grid(column=0,row=24)


window.mainloop()
