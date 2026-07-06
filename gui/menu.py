from tkinter import *
from operations.new_file import new
from operations.open_file import open_file
from operations.saveas_file import save_current
from operations.save_file import save_fill
from operations.edit import (
    undo,
    redo,
    cut,
    copy,
    paste,
    select_all,
    delete
)
from operations.dark_mode import dark_mode
def menu(window,wtext,label):
    wpad_menu  = Menu(window)
    window.config(menu=wpad_menu)

    #Menu File item
    def new_command():
        new(window,wtext,label)
    def open_command():
        open_file(window,wtext,label)
    def save_command():
        save_fill(window,wtext,label)
    def saveas_command():
        save_current(window,wtext,label)
    file_menu=Menu(wpad_menu)
    wpad_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="New",command=new_command)
    file_menu.add_separator()
    file_menu.add_command(label="Open",command=open_command)
    file_menu.add_separator()
    file_menu.add_command(label="Save",command=save_command)
    file_menu.add_separator()
    file_menu.add_command(label="Save As",command=saveas_command)

    #Menu edit item
    def undo_command():
         undo(wtext)
    def redo_command():
         redo(wtext)
    def cut_command():
         cut(wtext)
    def copy_command():
         copy(wtext)
    def paste_command():
         paste(wtext)
    edit_menu=Menu(wpad_menu)
    wpad_menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Undo",command=undo_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Redo",command=redo_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut",command=cut_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Copy",command=copy_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Paste",command=paste_command)

    #Menu view item
    def dark_command():
         dark_mode(window,wtext,label)
    def zoom_command():
         pass
    view_menu=Menu(wpad_menu)
    wpad_menu.add_cascade(label="View",menu=view_menu)
    view_menu.add_command(label="Dark mode",command=dark_command)
    view_menu.add_separator()
    view_menu.add_command(label="Zoom",command=zoom_command)
    
    #Menu tools item
    def word_command():
         pass
    def font_command():
         pass
    tools_menu=Menu(wpad_menu)
    wpad_menu.add_cascade(label="Tools",menu=tools_menu)
    tools_menu.add_command(label="Word Count",command=word_command)
    tools_menu.add_separator()
    tools_menu.add_command(label="Font",command=font_command)
    
    #Menu Help item
    def about_command():
         pass
    help_menu=Menu(wpad_menu)
    wpad_menu.add_cascade(label="Help",menu=help_menu)
    help_menu.add_command(label="About",command=about_command)

    