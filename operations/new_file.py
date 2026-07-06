from tkinter import *

def new(window, text_area, label):
    text_area.delete("1.0", END)
    window.title("PyPad - Untitled")
    label.config(text="Untitled")