import re
import tkinter as tk
import tkinter.ttk as ttk

from models.email import Email
from controllers.email import email_manager


class SendEmailWindow(tk.Tk):
    def __init__(self, parent, sender):
        self.parent = parent
        self.sender = sender

        self.root = tk.Toplevel(self.parent, padx=10, pady=10)
        self.root.title("New Email")

        width = 800
        height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.btn_send = ttk.Button(self.root, text="Send", command=self.send_email)
        self.btn_send.grid(row=0, column=1, padx=2, sticky="e")

        self.lbl_recipient = tk.Label(self.root, text="To")
        self.lbl_recipient.grid(row=1, column=0, sticky="w")

        self.txt_recipient = tk.Entry(self.root)
        self.txt_recipient.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

        self.lbl_subject = tk.Label(self.root, text="Subject")
        self.lbl_subject.grid(row=2, column=0, sticky="w")

        self.txt_subject = tk.Entry(self.root)
        self.txt_subject.grid(row=2, column=1, padx=(10, 0), pady=5, sticky="ew")

        self.txt_content = tk.Text(self.root)
        self.txt_content.grid(row=3, column=0, columnspan=2, sticky="nsew")

    def send_email(self):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

        recipient = self.txt_recipient.get()

        if not re.fullmatch(regex, recipient):
            return self.txt_recipient.config(highlightbackground="red")

        email = Email(
            sender=self.sender,
            recipient=recipient,
            subject=self.txt_subject.get(),
            content=self.txt_content.get("1.0", tk.END),
            priority=1,
        )

        email_manager.send_email(email)

        # Close window.
        self.root.destroy()
