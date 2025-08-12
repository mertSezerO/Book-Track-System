import tkinter as tk
from tkinter import ttk

from .page import Page
from controllers import LibraryController, ShelfController, BookController
from util import Colour


class CreateBookPage(Page):
    MAX_LABEL_WIDTH = 16

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value, width=400)
        self.header_frame.grid(row=0, column=1, pady=5, sticky="ew")

        self.title_label = tk.Label(
            self.header_frame,
            text="ADD NEW BOOK",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 32),
            bg=Colour.HEADER_BG_COLOUR.value,
            width=self.MAX_LABEL_WIDTH,
        )
        self.title_label.pack(pady=5)

        self.widget_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.keyword_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.button_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value, width=300)

        self.widget_frame.grid(row=1, column=1, pady=10)
        self.keyword_frame.grid(row=1, column=2, pady=10)
        self.button_frame.grid(row=2, column=1, pady=10)

        library_label = tk.Label(
            self.widget_frame,
            text="Select a Library",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
            width=self.MAX_LABEL_WIDTH,
        )
        library_label.pack(pady=5)

        self.libraries = LibraryController.get_libraries()
        self.library_dropdown_list = [library.name for library in self.libraries]

        self.selected_library = tk.StringVar()
        self.library_dropdown = ttk.Combobox(
            self.widget_frame,
            textvariable=self.selected_library,
            values=self.library_dropdown_list,
            postcommand=self.filter_shelves,
            style="Custom.TCombobox",
            width=80,
            height=10,
        )
        self.library_dropdown.pack(pady=5)

        shelf_label = tk.Label(
            self.widget_frame,
            text="Select a Shelf",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
            width=self.MAX_LABEL_WIDTH,
        )
        shelf_label.pack(pady=5)

        self.shelf_dropdown_list = None

        self.selected_shelf = tk.StringVar()
        self.shelf_dropdown = ttk.Combobox(
            self.widget_frame,
            textvariable=self.selected_shelf,
            values=self.shelf_dropdown_list,
            postcommand=self.filter_shelves,
            style="Custom.TCombobox",
            width=80,
            height=10,
        )
        self.shelf_dropdown.pack(pady=5)

        name_label = tk.Label(
            self.widget_frame,
            text="Name",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
            width=self.MAX_LABEL_WIDTH,
        )
        name_label.pack(pady=5)

        self.name_entry = tk.Entry(
            self.widget_frame,
            width=40,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.name_entry.pack(pady=5)

        author_label = tk.Label(
            self.widget_frame,
            text="Author",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
            width=self.MAX_LABEL_WIDTH,
        )
        author_label.pack(pady=5)

        self.author_entry = tk.Entry(
            self.widget_frame,
            width=40,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.author_entry.pack(pady=5)

        category_label = tk.Label(
            self.widget_frame,
            text="Category",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
            width=self.MAX_LABEL_WIDTH,
        )
        category_label.pack(pady=5)

        self.category_entry = tk.Entry(
            self.widget_frame,
            width=40,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
        )
        self.category_entry.pack(pady=5)

        self.keyword_entries = []
        self.keyword_button = tk.Button(
            self.button_frame,
            text="Add Keyword",
            command=self.add_keyword,
            font=("Arial", 16),
            bg=Colour.HEADER_TEXT_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.back_button = tk.Button(
            self.button_frame,
            text="Back",
            command=self.window.back_to_landing_page,
            font=("Arial", 16),
            bg=Colour.HEADER_TEXT_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.save_button = tk.Button(
            self.button_frame,
            text="Save",
            command=self.save_record,
            font=("Arial", 16),
            bg=Colour.HEADER_TEXT_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)

        self.keyword_button.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
        self.back_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.save_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

    def add_keyword(self):
        label = tk.Label(
            self.keyword_frame,
            text="Keyword " + str(len(self.keyword_entries) + 1),
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", 16),
            width=self.MAX_LABEL_WIDTH,
        )
        label.pack(pady=5)

        entry = tk.Entry(
            self.keyword_frame,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 16),
            width=40,
        )
        entry.pack(pady=5)

        self.keyword_entries.append(entry)

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
        keywords = [keyword.get() for keyword in self.keyword_entries]
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
            keywords=keywords,
        )
