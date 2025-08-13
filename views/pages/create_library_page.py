import tkinter as tk
from tkinter import ttk

from .page import Page
from controllers import LibraryController
from util import Colour


class CreateLibraryPage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value)
        self.header_frame.pack(pady=50)

        self.title_label = tk.Label(
            self.header_frame,
            text="CREATE NEW LIBRARY",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 32),
            bg=Colour.HEADER_BG_COLOUR.value,
        )
        self.title_label.pack(pady=10)

        self.widget_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.widget_frame.pack(pady=100)

        label = tk.Label(
            self.widget_frame,
            text="Name",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
        )
        label.pack(pady=10)

        self.entry = tk.Entry(
            self.widget_frame,
            width=50,
            font=("Arial", 16),
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.entry.pack(pady=10)

        self.save_button = tk.Button(
            self, text="Save", font=("Arial", 16), command=self.save_record,bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.save_button.pack(pady=10)

        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 16),
            command=self.window.back_to_landing_page,bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.back_button.pack(pady=10)

    def save_record(self):
        name = self.entry.get()
        LibraryController.create_library(name)
