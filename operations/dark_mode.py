from tkinter import *

def dark_mode(window, text_area, label):
    
    window.config(bg="black")

    
    text_area.config(
        bg="black",
        fg="white",
        insertbackground="white",      
        selectbackground="#4040ff",    
        selectforeground="white"
    )

    
    label.config(
        bg="black",
        fg="white"
    )