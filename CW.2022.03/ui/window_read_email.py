import tkinter as tk


class ReadEmailWindow(tk.Tk):
    def __init__(self, parent, email):
        self.parent = parent
        self.email = email

        self.root = tk.Toplevel(self.parent, padx=10, pady=10)
        self.root.title(self.email.subject)

        width = 800
        height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.lbl_sender = tk.Label(self.root, text="From")
        self.lbl_sender.grid(row=0, column=0, sticky="w")

        self.txt_sender = tk.Entry(self.root)
        self.txt_sender.grid(row=0, column=1, padx=(10, 0), pady=5, sticky="ew")
        self.txt_sender.insert(0, email.sender)
        self.txt_sender.config(state="disabled")

        self.lbl_subject = tk.Label(self.root, text="Subject")
        self.lbl_subject.grid(row=1, column=0, sticky="w")

        self.txt_subject = tk.Entry(self.root)
        self.txt_subject.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")
        self.txt_subject.insert(0, email.subject)
        self.txt_subject.config(state="disabled")

        self.txt_content = tk.Text(self.root)
        self.txt_content.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.txt_content.insert(tk.END, email.content)
        self.txt_content.config(state="disabled")
