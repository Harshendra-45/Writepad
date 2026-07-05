from tkinter import *
from tkinter import filedialog
from tkinter import font
def text_editor(window):
    w_frame = Frame(window)
    w_frame.pack(fill=BOTH, expand=True)
    text_scroll = Scrollbar(w_frame)
    text_scroll.pack(side=RIGHT,fill=Y)
    wtext=Text(w_frame,font=("Helvetica",20),selectbackground="blue",selectforeground="yellow",undo=True,yscrollcommand=text_scroll.set)
    wtext.pack(side=LEFT, fill=BOTH, expand=True)
    text_scroll.config(command=wtext.yview)
    
