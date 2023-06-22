import tkinter as tk
import tkinter.ttk as ttk


class ReadEmailWindow(tk.Tk):
    def __init__(self, parent, email):
        self.parent = parent
        self.email = email

        self.root = tk.Toplevel(self.parent)
        self.root.title("Email Detail")

        window_width = 800
        window_height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.txt_content = tk.Text(self.root, width=window_width, height=window_height)
        self.txt_content.grid(row=0, column=0)
        self.txt_content.insert(tk.END, email)

        self.root.protocol("WM_DELETE_WINDOW", self.close_windows)

    def close_windows(self):
        self.root.destroy()  # Destroy the second window
