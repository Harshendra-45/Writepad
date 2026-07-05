from tkinter import * 
from gui.menu import menu
from gui.text_editor import text_editor
from gui.statusbar import stat_bar
def show_window(): 
    window = Tk()
    window.geometry("800x600")
    window.title("Writepad")

    icon = PhotoImage(file='writepadlogo.png')
    window.iconphoto(True,icon)
    window.config(background='black')
    
    
    label = stat_bar(window)
    wtext = text_editor(window)    
    menu(window,wtext,label)
    


    window.mainloop()


