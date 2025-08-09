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
            )
            self.dropdown.pack(pady=10)

        # for column in self.model_columns:
