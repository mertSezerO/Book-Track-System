import tkinter as tk
from tkinter import ttk

from .page import Page
from controllers import LibraryController, ShelfController, BookController
from util import Colour


class CreateBookPage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value)
        self.header_frame.pack(pady=50)

        self.title_label = tk.Label(
            self.header_frame,
            text="ADD NEW BOOK",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 32),
            bg=Colour.HEADER_BG_COLOUR.value,
        )
        self.title_label.pack(pady=10)

        self.widget_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.widget_frame.pack(pady=20)

        library_label = tk.Label(
            self.widget_frame,
            text="Select a Library",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
        )
        library_label.pack(pady=10)

        self.libraries = LibraryController.get_libraries()
        self.library_dropdown_list = [library.name for library in self.libraries]

        self.selected_library = tk.StringVar()
        self.library_dropdown = ttk.Combobox(
            self.widget_frame,
            textvariable=self.selected_library,
            values=self.library_dropdown_list,
            postcommand=self.filter_shelves,
            style="Custom.TCombobox",
            width=100,
            height=10,
        )
        self.library_dropdown.pack(pady=10)

        shelf_label = tk.Label(
            self.widget_frame,
            text="Select a Shelf",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
        )
        shelf_label.pack(pady=10)

        self.shelf_dropdown_list = None

        self.selected_shelf = tk.StringVar()
        self.shelf_dropdown = ttk.Combobox(
            self.widget_frame,
            textvariable=self.selected_shelf,
            values=self.shelf_dropdown_list,
            postcommand=self.filter_shelves,
            style="Custom.TCombobox",
            width=100,
            height=10,
        )
        self.shelf_dropdown.pack(pady=10)

        name_label = tk.Label(
            self.widget_frame,
            text="Name",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
        )
        name_label.pack(pady=10)

        self.name_entry = tk.Entry(
            self.widget_frame,
            width=50,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.name_entry.pack(pady=10)

        author_label = tk.Label(
            self.widget_frame,
            text="Author",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
        )
        author_label.pack(pady=10)

        self.author_entry = tk.Entry(
            self.widget_frame,
            width=50,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.author_entry.pack(pady=10)

        category_label = tk.Label(
            self.widget_frame,
            text="Category",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
        )
        category_label.pack(pady=10)

        self.category_entry = tk.Entry(
            self.widget_frame,
            width=50,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.category_entry.pack(pady=10)

        self.back_button = tk.Button(
            self,
            text="Back",
            command=self.window.back_to_landing_page,
            font=("Arial", 16),
        )
        self.back_button.pack(pady=10)

        self.save_button = tk.Button(
            self,
            text="Save",
            command=self.save_record,
            font=("Arial", 16),
        )
        self.save_button.pack(pady=10)

    def filter_shelves(self):
        if self.selected_library.get() == "":
            return

        library = next(
            (lib for lib in self.libraries if lib.name == self.selected_library.get()),
            None,
        )
        if library is None:
            raise ReferenceError("Selected library is not exists!")

        self.shelves = ShelfController.gather_library_shelves_by_id(
            library_id=library.library_id
        )
        self.shelf_dropdown_list = [shelf.name for shelf in self.shelves]
        self.shelf_dropdown["values"] = self.shelf_dropdown_list

    def save_record(self):
        book_name = self.name_entry.get()
        book_author = self.author_entry.get()
        book_category = self.category_entry.get()

        shelf = next(
            (
                shelf
                for shelf in self.shelves
                if shelf.name == self.selected_shelf.get()
            ),
            None,
        )
        if shelf is None:
            raise ReferenceError("Selected library is not exists!")

        BookController.add_book(
            name=book_name,
            author=book_author,
            category=book_category,
            shelf_id=shelf.shelf_id,
        )
