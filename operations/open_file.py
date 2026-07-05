from tkinter import *
from tkinter import filedialog
from utils import state
def open_file(window,text_area,label):
    text_area.delete("1.0", END)
    txt_file =filedialog.askopenfilename(initialdir="D:/wp/",title="Open File",filetypes=(("Text FIles","*.txt"),("All Files","*.*")))
    if txt_file:
        state.current_file=txt_file
    name = txt_file
    label.config(text=name)
    name = name.replace("D:/wp/","")
    window.title((f"WritePad - {name}"))
    txt_file = open(txt_file, "r", encoding="utf-8")
    stuff=txt_file.read()
    text_area.insert(END,stuff)
    txt_file.close()

    