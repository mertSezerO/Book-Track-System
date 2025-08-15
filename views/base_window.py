import tkinter as tk
from tkinter import ttk

from copy import deepcopy

from util import Colour
from .pages.landing_page import LandingPage, Page


class BaseWindow:
    def __init__(self, title="Book Tracker", width=1600, height=1600):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        dropdown_style = ttk.Style()
        dropdown_style.theme_use("clam")
        dropdown_style.configure(
            "Custom.TCombobox",
            fieldbackground=Colour.HEADER_TEXT_COLOUR.value,
            background=Colour.DROPDOWN_COLOUR.value,
            foreground=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 24),
        )

        self.show_landing_page()

    def show_landing_page(self):
        self.previous_page = None
        self.current_page = LandingPage(self.root, self)

    def switch_pages(self, new_page: Page = None, page_params=None):
        self.previous_page = self.current_page
        self.current_page.pack_forget()
        if new_page:
            if page_params:
                self.current_page = new_page(self.root, self, page_params=page_params)
            else:
                self.current_page = new_page(self.root, self)
        else:
            self.current_page = LandingPage(self.root, self)
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def show_previous_page(self):
        if self.previous_page:
            self.switch_pages(self.previous_page)

    def back_to_landing_page(self):
        self.current_page.pack_forget()
        self.current_page = LandingPage(self.root, self)
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()
