import tkinter as tk

from .page import Page
from util import Colour
from controllers import BookController
from .search_results_page import SearchResultsPage

class SearchPage(Page):
    LABEL_WIDTH = 16
    INPUT_WIDTH = 50
    FONT_SIZE = 16
    HEADER_FONT_SIZE = 32


    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg=Colour.HEADER_BG_COLOUR.value, width=400)
        self.header_frame.grid(row=0, column=1, pady=5)

        self.title_label = tk.Label(
            self.header_frame,
            text="SEARCH BOOK",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.HEADER_FONT_SIZE),
            bg=Colour.HEADER_BG_COLOUR.value,
            width=self.LABEL_WIDTH,
        )
        self.title_label.pack(pady=5)

        self.search_frame = tk.Frame(self, bg=Colour.HEADER_TEXT_COLOUR.value, width=600)
        self.search_frame.grid(row=1, column=1, pady=20, sticky="ew")

        search_label = tk.Label(
            self.search_frame,
            text="Search Criteria",
            bg=Colour.HEADER_TEXT_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE, "bold"),
            width=self.LABEL_WIDTH,
        )
        search_label.pack(pady=5)

        self.search_entry = tk.Entry(
            self.search_frame,
            width=self.INPUT_WIDTH,
            borderwidth=2,
            relief="sunken",
            bg=Colour.DROPDOWN_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", self.FONT_SIZE),
        )
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(
            self.search_frame,
            text="Submit",
            command=self.search_by_criteria,
            font=("Arial", self.FONT_SIZE),
            bg=Colour.ACTION_BUTTON_COLOUR.value,
            fg=Colour.HEADER_TEXT_COLOUR.value,
        )
        self.search_button.pack(pady=10)

        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 16),
            command=self.window.back_to_landing_page,bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.back_button.grid(row=2,column=1,pady=10)

    def search_by_criteria(self):
        search_input = self.search_entry.get()
        if search_input:
            criterias = search_input.split(" ")
            query = {}
            for criteria in criterias:
                key,value = criteria.split(":")
                if not BookController.check_column_name(key):
                    raise Exception("{} not a valid criteria!".format(key))
                query[key] = value
    
            results = BookController.search_books_by_criteria(query)
        
        else:
            results = BookController.search_books_by_criteria()
        self.window.switch_pages(new_page=SearchResultsPage, page_params=results)
        