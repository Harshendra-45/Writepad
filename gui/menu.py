from tkinter import *
def menu(name):
    wpad_menu  = Menu(name)
    name.config(menu=wpad_menu)

    #Menu File item
    def new_command():
        pass
    def open_command():
        pass
    def save_command():
        pass
    def saveas_command():
        pass
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
        pass
    def redo_command():
        pass
    def cut_command():
            pass
    def copy_command():
         pass
    def paste_command():
         pass
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
    def white_command():
         pass
    def zoom_command():
         pass
    view_menu=Menu(wpad_menu)
    wpad_menu.add_cascade(label="View",menu=view_menu)
    view_menu.add_command(label="White mode",command=white_command)
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

    