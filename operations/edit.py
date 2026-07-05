def undo(text_area):
    text_area.event_generate("<<Undo>>")


def redo(text_area):
    text_area.event_generate("<<Redo>>")


def cut(text_area):
    text_area.event_generate("<<Cut>>")


def copy(text_area):
    text_area.event_generate("<<Copy>>")


def paste(text_area):
    text_area.event_generate("<<Paste>>")


def select_all(text_area):
    text_area.tag_add("sel", "1.0", "end")


def delete(text_area):
    text_area.delete("sel.first", "sel.last")