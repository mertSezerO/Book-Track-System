import tkinter as tk

from .common import Colour

class Notifier:

    def __init__(self, root):
        self.root = root

    def show_notification(self, message, duration=3000):
        toast = tk.Toplevel(self.root)
        toast.overrideredirect(True)
        toast.configure(bg=Colour.ACTION_BUTTON_COLOUR.value)
        
        x = (int)(self.root.winfo_x() + self.root.winfo_width() / 2) - 200
        y = (int)(self.root.winfo_y() + self.root.winfo_height() / 4)
        toast.geometry(f"400x50+{x}+{y}")
        
        label = tk.Label(toast, text=message, fg=Colour.HEADER_TEXT_COLOUR.value, bg=Colour.ACTION_BUTTON_COLOUR.value, font=("Arial", 16))
        label.pack(expand=True, fill="both")
        
        toast.after(duration, toast.destroy)