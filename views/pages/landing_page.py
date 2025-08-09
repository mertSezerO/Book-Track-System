import tkinter as tk

from .page import Page
from util import Colour


class LandingPage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.config(bg=Colour.BACKGROUND_COLOUR.value)

        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value)
        self.header_frame.pack(pady=10)

        self.title_label = tk.Label(
            self.header_frame,
            text="WELCOME TO ISKENDERIYE DB",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 24),
            bg=Colour.HEADER_BG_COLOUR.value,
        )
        self.title_label.pack(pady=10)

        self.search_button = tk.Button(
            self,
            text="SEARCH",
            command=None,
            width=20,
            height=2,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            activebackground=Colour.WIDGET_ACTION_COLOUR.value,
            activeforeground=Colour.BACKGROUND_COLOUR.value,
        )
        self.search_button.pack(pady=5)

        self.add_button = tk.Button(
            self,
            text="ADD",
            command=None,
            width=20,
            height=2,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            activebackground=Colour.WIDGET_ACTION_COLOUR.value,
            activeforeground=Colour.BACKGROUND_COLOUR.value,
        )
        self.add_button.pack(pady=5)
