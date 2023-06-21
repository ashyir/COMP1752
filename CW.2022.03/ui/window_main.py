import tkinter as tk

from ui.frame_login import LoginFrame
from ui.frame_email_list import EmailListFrame


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.show_frame(LoginFrame)

    def show_frame(self, frame_classname):
        frame = frame_classname(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_email_list_frame(self, is_authenticated):
        if is_authenticated:
            self.show_frame(EmailListFrame)

    def show_login_frame(self):
        self.show_frame(LoginFrame)
