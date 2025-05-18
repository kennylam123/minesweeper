from tkinter import Button

def create_button(parent,text,command=None,width=20,**kwargs):
    return Button(
        parent,
        text=text,
        width=width,
        command=command,
        **kwargs
    )