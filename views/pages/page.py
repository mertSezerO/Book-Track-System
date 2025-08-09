import tkinter as tk

from util import Colour


class Page(tk.Frame):
    def __init__(self, parent, window):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.config(bg=Colour.BACKGROUND_COLOUR.value)
        self.window = window
