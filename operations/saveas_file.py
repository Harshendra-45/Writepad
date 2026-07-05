from tkinter import *
from tkinter import filedialog,messagebox
def save_current(window,text_area,label):
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="D:/wp/",title="Save File",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    if text_file:
        name = text_file
        label.config(text=f'Saved At:{name}')
        name = name.replace("D:/wp/","")
        window.title((f"WritePad - {name}"))
        text_file=open(text_file,'w')
        text_file.write(text_area.get(1.0,END))
        text_file.close()
