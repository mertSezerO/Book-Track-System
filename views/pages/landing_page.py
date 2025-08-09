import tkinter as tk

from .page import Page


class LandingPage(Page):

    def __init__(self, parent, window):
        super().__init__(parent, window)

        self.title_label = tk.Label(self, text="Courses", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.course_buttons_frame = tk.Frame(self)
        self.course_buttons_frame.pack(pady=10)

        self.add_course_button = tk.Button(
            self, text="Yeni Kurs Ekle", command=self.add_course, width=20, height=2
        )
        self.add_course_button.pack(pady=5)
