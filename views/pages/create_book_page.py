import tkinter as tk
from tkinter import ttk

from .page import Page
from controllers import LibraryController, ShelfController, BookController
from util.common import Colour


class CreateBookPage(Page):
    LABEL_WIDTH = 16
    INPUT_WIDTH = 50
    FONT_SIZE = 14
    HEADER_FONT_SIZE = 32

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value, width=400)
        self.header_frame.grid(row=0, column=1, pady=20, sticky="ew")

        self.title_label = tk.Label(
            self.header_frame,
            text="ADD NEW BOOK",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.HEADER_FONT_SIZE),
            bg=Colour.HEADER_BG_COLOUR.value,
            width=self.LABEL_WIDTH,
        )
        self.title_label.pack(pady=5)

        self.widget_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.keyword_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)
        self.button_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value, width=300)
        self.keyword_button_frame = tk.Frame(self, bg=Colour.BACKGROUND_COLOUR.value)

        self.widget_frame.grid(row=1, column=1, pady=10)
        self.keyword_frame.grid(row=1, column=2, pady=10)
        self.button_frame.grid(row=2, column=1, pady=10)
        self.keyword_button_frame.grid(row=2, column=2, pady=10)

        library_label = tk.Label(
            self.widget_frame,
            text="Select a Library",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
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
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
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

        self.entries = []
        name_label = tk.Label(
            self.widget_frame,
            text="Name",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
        )
        name_label.pack(pady=5)

        self.name_entry = tk.Entry(
            self.widget_frame,
            width=self.INPUT_WIDTH,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            borderwidth=2,
            relief="sunken",
        )
        self.name_entry.pack(pady=5)
        self.entries.append(self.name_entry)

        author_label = tk.Label(
            self.widget_frame,
            text="Author",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
        )
        author_label.pack(pady=5)

        self.author_entry = tk.Entry(
            self.widget_frame,
            width=self.INPUT_WIDTH,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            borderwidth=2,
            relief="sunken",
        )
        self.author_entry.pack(pady=5)
        self.entries.append(self.author_entry)

        category_label = tk.Label(
            self.widget_frame,
            text="Category",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
        )
        category_label.pack(pady=5)

        self.category_entry = tk.Entry(
            self.widget_frame,
            width=self.INPUT_WIDTH,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            borderwidth=2,
            relief="sunken",
        )
        self.category_entry.pack(pady=5)
        self.entries.append(self.category_entry)

        translator_label = tk.Label(
            self.widget_frame,
            text="Translator",
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
        )
        translator_label.pack(pady=5)
        self.translator_entry = tk.Entry(
            self.widget_frame,
            width=self.INPUT_WIDTH,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            borderwidth=2,
            relief="sunken",
        )
        self.translator_entry.pack(pady=5)
        self.entries.append(self.translator_entry)

        self.keyword_entries = []
        self.keyword_labels = []
        self.keyword_add_button = tk.Button(
            self.button_frame,
            text="Add Keyword",
            command=self.add_keyword,
            font=("Arial", self.FONT_SIZE),
            bg=Colour.ACTION_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.save_button = tk.Button(
            self.button_frame,
            text="Save",
            command=self.save_record,
            font=("Arial", self.FONT_SIZE),
            bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.back_button = tk.Button(
            self.button_frame,
            text="Back",
            command=self.window.back_to_landing_page,
            font=("Arial", self.FONT_SIZE),
            bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)

        self.keyword_delete_button = tk.Button(
            self.keyword_button_frame,
            text="Remove Keyword",
            command=self.remove_keyword,
            font=("Arial", self.FONT_SIZE),
            bg=Colour.ACTION_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )

        self.keyword_add_button.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
        self.save_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.back_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

    def add_keyword(self):
        self.keyword_frame.grid(row=1, column=2, pady=10)
        label = tk.Label(
            self.keyword_frame,
            text="Keyword " + str(len(self.keyword_entries) + 1),
            bg=Colour.HEADER_BG_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.LABEL_WIDTH,
        )
        label.pack(pady=5)

        entry = tk.Entry(
            self.keyword_frame,
            bg=Colour.WIDGET_BG_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
            width=self.INPUT_WIDTH,
            borderwidth=2,
            relief="sunken",
        )
        entry.pack(pady=5)

        self.keyword_entries.append(entry)
        self.keyword_labels.append(label)
        self.keyword_button_frame.grid(row=2, column=2, pady=10)
        self.keyword_delete_button.pack(pady=5)
    
    def remove_keyword(self):
        self.keyword_entries[len(self.keyword_entries) - 1].destroy()
        self.keyword_labels[len(self.keyword_labels) - 1].destroy()

        self.keyword_entries.pop(len(self.keyword_entries) - 1)
        self.keyword_labels.pop(len(self.keyword_entries) - 1)

        if len(self.keyword_entries) == 0:
            self.keyword_delete_button.pack_forget()
            self.keyword_button_frame.grid_forget()
            self.keyword_frame.grid_forget()

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
        try:
            book_name = self.name_entry.get()
            book_author = self.author_entry.get()
            book_category = self.category_entry.get()
            translator = self.translator_entry.get()

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

            result = BookController.add_book(
                name=book_name,
                author=book_author,
                category=book_category,
                translator=translator,
                shelf_id=shelf.shelf_id,
                keywords=keywords,
            )

            if not result.success:
                raise Exception(result.message)

            self.clear_widgets()
            self.window.notifier.show_notification(message=result.message)

        except Exception as e:
            self.window.notifier.show_notification(message=e)

    def clear_widgets(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        
        for entry in self.keyword_entries:
            entry.delete(0, tk.END)

        self.shelf_dropdown.set("")
        self.library_dropdown.set("")

        self.keyword_delete_button.pack_forget()
        self.keyword_button_frame.grid_forget()
        self.keyword_frame.grid_forget()