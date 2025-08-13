import tkinter as tk

from .page import Page
from .create_library_page import CreateLibraryPage
from .create_shelf_page import CreateShelfPage
from .create_book_page import CreateBookPage
from .search_page import SearchPage
from util import Colour
from models import Library, Shelf, Book


class LandingPage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value)
        self.header_frame.pack(pady=50)

        self.title_label = tk.Label(
            self.header_frame,
            text="WELCOME TO ISKENDERIYE DB",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 32),
            bg=Colour.HEADER_BG_COLOUR.value,
        )
        self.title_label.pack(pady=10)

        self.widget_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.widget_frame.pack(pady=100)

        self.search_button = tk.Button(
            self.widget_frame,
            text="SEARCH",
            command=self.switch_to_search,
            width=20,
            height=2,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            activebackground=Colour.WIDGET_ACTION_COLOUR.value,
            activeforeground=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.search_button.pack(pady=5)

        self.add_library_button = tk.Button(
            self.widget_frame,
            text="CREATE LIBRARY",
            command=self.switch_to_create_library,
            width=20,
            height=2,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            activebackground=Colour.WIDGET_ACTION_COLOUR.value,
            activeforeground=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.add_library_button.pack(pady=5)

        self.add_shelf_button = tk.Button(
            self.widget_frame,
            text="ADD SHELF",
            command=self.switch_to_add_shelf,
            width=20,
            height=2,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            activebackground=Colour.WIDGET_ACTION_COLOUR.value,
            activeforeground=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.add_shelf_button.pack(pady=5)

        self.add_book_button = tk.Button(
            self.widget_frame,
            text="ADD BOOK",
            command=self.switch_to_add_book,
            width=20,
            height=2,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            activebackground=Colour.WIDGET_ACTION_COLOUR.value,
            activeforeground=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.add_book_button.pack(pady=5)

    def switch_to_create_library(self):
        self.window.switch_pages(new_page=CreateLibraryPage)

    def switch_to_add_shelf(self):
        self.window.switch_pages(new_page=CreateShelfPage)

    def switch_to_add_book(self):
        self.window.switch_pages(new_page=CreateBookPage)

    def switch_to_search(self):
        self.window.switch_pages(new_page=SearchPage)
