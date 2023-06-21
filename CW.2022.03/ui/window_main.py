import tkinter as tk

from ui.frame_login import LoginFrame
from ui.frame_email_list import EmailListFrame


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginFrame, EmailListFrame):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def login(self, is_authenticated):
        if is_authenticated:
            self.show_frame(EmailListFrame)
