import tkinter as tk
from tkinter import ttk

from .page import Page
from util import Colour
from controllers import BookController

class SearchResultsPage(Page):
    LABEL_WIDTH = 16
    INPUT_WIDTH = 50
    FONT_SIZE = 16
    HEADER_FONT_SIZE = 32


    def __init__(self, parent, window, page_params: list):
        super().__init__(parent, window)
        self.table_data = BookController.convert_to_table_data(page_params)

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
            text="SEARCH RESULTS",
            fg=Colour.HEADER_TEXT_COLOUR.value,
            font=("Arial", self.HEADER_FONT_SIZE),
            bg=Colour.HEADER_BG_COLOUR.value,
            width=self.LABEL_WIDTH,
        )
        self.title_label.pack(pady=5)

        self.result_frame = tk.Frame(self, bg=Colour.HEADER_TEXT_COLOUR.value, width=1000, height=1000)
        self.result_frame.grid(row=1, column=1, pady=20, sticky="ew")

        self.tree = ttk.Treeview(self.result_frame, columns=self.table_data.columns, show="headings", style="Custom.Treeview")

        for col in self.table_data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=200)

        for i, row in enumerate(self.table_data.get_data()):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", tk.END, values=row, tags=(tag,))

        self.tree.tag_configure("oddrow", background=Colour.WIDGET_BG_COLOUR.value)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 16),
            command=self.window.back_to_landing_page,bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.back_button.grid(row=2,column=1,pady=10)

        
