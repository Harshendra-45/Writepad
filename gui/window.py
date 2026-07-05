from tkinter import * 
from menu import menu
from text_editor import text_editor
from statusbar import stat_bar
def show_window(): 
    window = Tk()
    window.geometry("800x600")
    window.title("Writepad")

    icon = PhotoImage(file='writepadlogo.png')
    window.iconphoto(True,icon)
    window.config(background='black')
    
    
    menu(window)
    stat_bar(window)
    text_editor(window)   
    


    window.mainloop()

show_window()
