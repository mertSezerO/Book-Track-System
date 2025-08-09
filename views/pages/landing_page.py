import tkinter as tk

from .page import Page


class LandingPage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)
        self.config(bg="#2c3e50")

        self.title_label = tk.Label(
            self, text="WELCOME TO ISKENDERIYE DB", font=("Arial", 24)
        )
        self.title_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self, bg="#2c3e50")
        self.buttons_frame.pack(pady=10)

        self.search_button = tk.Button(
            self,
            text="SEARCH",
            command=None,
            width=20,
            height=2,
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
        )
        self.search_button.pack(pady=5)

        self.add_button = tk.Button(
            self,
            text="ADD",
            command=None,
            width=20,
            height=2,
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
        )
        self.add_button.pack(pady=5)
