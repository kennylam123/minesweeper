import tkinter as tk

class popups(tk.Toplevel):
    def __init__(self,parent,title="popup", message=" ", buttons=None):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x150")
        self.configure(bg="white")
        self.resizable(False,False)
        self.trasient(parent)
        self.grab_set()