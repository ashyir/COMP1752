import tkinter as tk
import tkinter.ttk as ttk

from view_login import LoginPage


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main Page")
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Logout", command=lambda: controller.show_frame(LoginPage)
        )

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)
