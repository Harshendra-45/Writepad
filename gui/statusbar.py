from tkinter import *

def stat_bar(window):
    stat = Label(
        window,
        text="Ready",
        bg="grey",
        fg="white",
        relief=SUNKEN
    )
    stat.pack(side=BOTTOM, fill=X)