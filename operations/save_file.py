from tkinter import *
from tkinter import filedialog,messagebox
from utils import state
def save_fill(window,text_area,label):
    if state.current_file:
        text_file=open(state.current_file,'w')
        text_file.write(text_area.get(1.0,END))
        text_file.close()
        label.config(text=f'Saved At:{state.current_file}')
    else:
        text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="D:/wp/",title="Save File",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
        if text_file:
            name = text_file
            label.config(text=f'Saved At:{name}')
            name = name.replace("D:/wp/","")
            window.title((f"WritePad - {name}"))
            text_file=open(text_file,'w')
            text_file.write(text_area.get(1.0,END))
            text_file.close()