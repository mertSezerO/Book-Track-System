import tkinter as tk
from tkinter import ttk

from util import Notifier, Logger, DatabaseConnector
from util.common import Colour, LogData
from .pages.landing_page import LandingPage, Page


class BaseWindow:
    def __init__(self, title="Book Tracker", width=1600, height=1600):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.notifier = Notifier(self.root)
        self.logger = Logger()

        self.set_styles()
        self.show_landing_page()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        DatabaseConnector.upload_backup(self.logger)

        self.logger.log(LogData(
            message="Application closed.",
            source="view",
            level="info"
        ))

        self.root.destroy()

    def set_styles(self):
        dropdown_style = ttk.Style()
        dropdown_style.theme_use("clam")
        dropdown_style.configure(
            "Custom.TCombobox",
            fieldbackground=Colour.HEADER_TEXT_COLOUR.value,
            background=Colour.DROPDOWN_COLOUR.value,
            foreground=Colour.BACKGROUND_COLOUR.value,
            font=("Arial", 24),
        )

        table_style = ttk.Style()
        table_style.theme_use("clam")
        table_style.configure(
            "Custom.Treeview",
            background=Colour.DROPDOWN_COLOUR.value,
            foreground=Colour.BACKGROUND_COLOUR.value,
            fieldbackground=Colour.HEADER_TEXT_COLOUR.value ,
            font=("Arial", 14),
            rowheight=40
        )
        table_style.configure(
            "Custom.Treeview.Heading",
            font=("Arial", 18, "bold"),
            background=Colour.ACTION_BUTTON_COLOUR.value,
            foreground=Colour.HEADER_TEXT_COLOUR.value,
        )

        scroll_style = ttk.Style()
        scroll_style.theme_use("clam")
        scroll_style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            troughcolor=Colour.BACKGROUND_COLOUR.value,
            background=Colour.ACTION_BUTTON_COLOUR.value,  
            darkcolor=Colour.ROUTE_BUTTON_COLOUR.value,
            lightcolor=Colour.ROUTE_BUTTON_COLOUR.value,
            arrowcolor=Colour.HEADER_TEXT_COLOUR.value
        )

        self.logger.log(LogData(
            message="Widgets created for page: {}",
            source="view",
            level="debug",
            args=("Window", )
        ))

    def show_landing_page(self):
        self.previous_page = None
        self.logger.log(LogData(
            message="Landing Page created for: {}",
            source="view",
            level="info",
            args=("Window", )
        ))
        self.current_page = LandingPage(self.root, self)

    def switch_pages(self, new_page: Page = None, **kwargs):
        self.previous_page = self.current_page
        self.current_page.pack_forget()
        if new_page:
            if kwargs:
                self.current_page = new_page(self.root, self, **kwargs)
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
        self.logger.log(LogData(
            message="Application ran successfully",
            source="view",
            level="info"
        ))
        self.root.mainloop()
