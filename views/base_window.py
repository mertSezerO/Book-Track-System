import tkinter as tk
from copy import deepcopy

from .pages.landing_page import LandingPage, Page


class BaseWindow:
    def __init__(self, title="Book Tracker", width=1600, height=1600):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.show_landing_page()

    def show_landing_page(self):
        self.previous_page = None
        self.current_page = LandingPage(self.root, self)

    def switch_pages(self, new_page: Page = None, options: dict = None):
        if options:
            self.__options = options
        self.previous_page = self.current_page
        self.current_page.pack_forget()
        if new_page:
            self.current_page = new_page(self.root, self)
        else:
            self.current_page = LandingPage(self.root, self)
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def show_previous_page(self):
        if self.previous_page:
            self.switch_pages(self.previous_page)

    def get_options(self):
        options = deepcopy(self.__options)
        del self.__options
        return options

    def run(self):
        self.root.mainloop()
