import tkinter as tk


class Page(tk.Frame):
    def __init__(self, parent, window):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.window = window
