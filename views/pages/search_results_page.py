import tkinter as tk
from tkinter import ttk

from .page import Page
from util.common import Colour, LogData
from controllers import BookController

class SearchResultsPage(Page):
    LABEL_WIDTH = 16
    INPUT_WIDTH = 50
    FONT_SIZE = 16
    HEADER_FONT_SIZE = 32


    def __init__(self, parent, window, **kwargs):
        super().__init__(parent, window)
        
        self.search_criteria = kwargs["search_input"]
        self.search_by_criteria()
        self.order_column = "Book ID"

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
            self.tree.heading(col, text=col, command=lambda column_name=col: self.order_by_column(column_name))
            self.tree.column(col, anchor="center", width=200)

        for i, row in enumerate(self.tree_data):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", tk.END, values=row, tags=(tag,))

        self.tree.tag_configure("oddrow", background=Colour.WIDGET_BG_COLOUR.value)
        vsb = ttk.Scrollbar(
            self.result_frame,
            orient="vertical",
            command=self.tree.yview,
            style="Vertical.TScrollbar"
        )
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack(side="left", fill=tk.BOTH, expand=True)
        vsb.pack(side="right", fill="y")

        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 16),
            command=self.window.back_to_landing_page,bg=Colour.ROUTE_BUTTON_COLOUR.value,
            fg=Colour.BACKGROUND_COLOUR.value,
        )
        self.back_button.grid(row=2,column=1,pady=10)

        self.window.logger.log(LogData(
            message="Widgets created for page: {}",
            source="view",
            level="debug",
            args=("SearchResultPage", )
        ))
        
    def search_by_criteria(self):
        if self.search_criteria:
            criterias = self.search_criteria.split(" ")
            query = {}
            for criteria in criterias:
                key,value = criteria.split(":")
                if not BookController.check_column_name(key):
                    raise Exception("{} not a valid criteria!".format(key))
                query[key] = value
    
            results = BookController.search_books_by_criteria(query)
        
        else:
            results = BookController.search_books_by_criteria()

        self.table_data = results
        self.tree_data = results.get_data()
        self.window.logger.log(LogData(
            message="Books fetched for page: {}, Result => Query={query} Number of Books:{size}",
            source="view",
            level="info",
            args=("SearchResultPage", ),
            kwargs={"query": self.search_criteria, "size": len(self.tree_data)}
        ))

    def order_by_column(self, column_name: str):
        if self.order_column == column_name:
            return
        
        self.order_column = column_name
        self.tree_data = self.table_data.sort_by_column(column_name)
        self.window.logger.log(LogData(
            message="Search table order for page: {}, Order By: {col}",
            source="view",
            level="info",
            args=("SearchResultPage", ),
            kwargs={"col": column_name}
        ))
        self.reform_table()

    def reform_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, row in enumerate(self.tree_data):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", tk.END, values=row, tags=(tag,))

        self.window.logger.log(LogData(
            message="Search table reset for action: {}, Order By: {col}",
            source="view",
            level="info",
            args=("SearchResultPage", ),
            kwargs={"col": self.order_column}
        ))