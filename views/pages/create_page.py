import tkinter as tk
from tkinter import ttk

from .page import Page
from controllers import ModelController, ShelfController, LibraryController
from util import Colour


class CreatePage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.parse_options()
        self.create_widgets()

    def parse_options(self):
        options = self.window.get_options()
        self.model_columns = ModelController.get_model_columns(options["class"])
        self.page_name = options["class"].__name__
        self.relation = options["relation"]

        if self.relation:
            if self.relation == "Library":
                self.dropdown_list = LibraryController.get_libraries()
            elif self.relation == "Shelf":
                self.dropdown_list = ShelfController.get_shelves()
            else:
                raise ValueError("Incorrect relation option!")

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value)
        self.header_frame.pack(pady=50)

        self.title_label = tk.Label(
            self.header_frame,
            text="CREATE NEW {}".format(self.page_name.upper()),
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 24),
            bg=Colour.HEADER_BG_COLOUR.value,
        )
        self.title_label.pack(pady=10)

        self.widget_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.widget_frame.pack(pady=100)

        self.back_button = tk.Button(
            self, text="Back", command=self.window.back_to_landing_page
        )
        self.back_button.pack(pady=10)

        if self.relation:
            self.drowdown_label = tk.Label(
                self.widget_frame, text="Select {}".format(self.relation)
            )
            self.drowdown_label.pack(pady=10)

            self.drowdown_selected = tk.StringVar()
            self.dropdown = ttk.Combobox(
                self.widget_frame,
                textvariable=self.drowdown_selected,
                values=self.dropdown_list,
                width=50,
                height=5,
            )
            self.dropdown.pack(pady=10)

        self.entries = []
        for column in self.model_columns:
            label = tk.Label(self.widget_frame, text=column.name)
            label.pack(pady=10)

            entry = tk.Entry(self.widget_frame, width=50)
            entry.pack(pady=10)
            self.entries.append(entry)

        self.save_button = tk.Button(self, text="Save", command=self.save_record)
        self.save_button.pack(pady=10)

    def save_record(self):
        pass
