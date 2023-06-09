import tkinter as tk
import tkinter.ttk as ttk

from models.email import Label

from controllers.email import email_manager
from controllers.account import account_manager

from ui.window_read_email import ReadEmailWindow
from ui.window_send_email import SendEmailWindow


class EmailListFrame(tk.Frame):
    columns = [
        "Id",
        "Priority",
        "From",
        "Label",
        "Subject",
    ]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.current_user_email = account_manager.current_user.email

        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # First row with all buttons.
        btn_new_email = ttk.Button(self, text="New Email", command=self.new_email)
        btn_new_email.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        btn_list_email = ttk.Button(
            self, text="Get All Emails", command=self.get_emails_by_current_user
        )
        btn_list_email.grid(row=0, column=1, padx=5, sticky="ew")

        btn_delete_email = ttk.Button(
            self, text="Delete Emails", command=self.delete_email
        )
        btn_delete_email.grid(row=0, column=2, padx=5, sticky="ew")

        self.cb_label = ttk.Combobox(self, values=[label.value for label in Label])
        self.cb_label.grid(row=0, column=3, padx=5, sticky="ew")
        self.cb_label.set(Label.STAR.value)

        btn_filter = ttk.Button(self, text="Filter", command=self.get_emails_by_label)
        btn_filter.grid(row=0, column=4, padx=5, sticky="ew")

        btn_add_label = ttk.Button(self, text="Add Label", command=self.add_label)
        btn_add_label.grid(row=0, column=5, padx=(5, 0), sticky="ew")

        # Second row with list of emails.
        self.email_list = ttk.Treeview(self, columns=self.columns, show="headings")
        self.email_list.grid(row=1, column=0, columnspan=6, pady=10, sticky="nsew")

        self.email_list.column("Id", width=50, anchor="center")
        self.email_list.column("Priority", width=50)

        for column in self.columns:
            self.email_list.heading(column, text=column)

        self.email_list.bind("<Double-Button-1>", self.read_email)

        self.get_emails_by_current_user()

        # Third row with status.
        lbl_status = ttk.Label(self, text=f"Current user is {self.current_user_email}.")
        lbl_status.grid(row=2, column=0, sticky="w")

        btn_logout = ttk.Button(
            self, text="Logout", command=lambda: controller.show_login_frame()
        )
        btn_logout.grid(row=2, column=5, sticky="e")

    def get_emails_by_current_user(self):
        self.email_list.delete(*self.email_list.get_children())

        for email in email_manager.get_emails_by_recipient(self.current_user_email):
            self.email_list.insert(
                "",
                tk.END,
                values=(
                    email.id,
                    "*" * email.priority,
                    email.sender,
                    email.labels,
                    email.subject,
                ),
            )

    def get_emails_by_label(self):
        self.email_list.delete(*self.email_list.get_children())

        label = self.cb_label.get()

        for email in email_manager.get_emails_by_label(label):
            self.email_list.insert(
                "",
                tk.END,
                values=(
                    email.id,
                    "*" * email.priority,
                    email.sender,
                    email.labels,
                    email.subject,
                ),
            )

    def new_email(self):
        SendEmailWindow(self.parent, self.current_user_email)

    def delete_email(self):
        selected_items = self.email_list.selection()

        for item in selected_items:
            try:
                email_id = int(self.email_list.item(item)["values"][0])
            except ValueError:
                email_id = -1

            is_deleted = email_manager.delete_email(email_id)

            if is_deleted:
                self.email_list.delete(item)

    def read_email(self, event):
        item_id = self.email_list.focus()
        values = self.email_list.item(item_id, "values")

        try:
            email_id = int(values[0])
        except ValueError:
            email_id = -1

        email = email_manager.read_email(email_id)

        if email is not None:
            ReadEmailWindow(self.parent, email)

    def add_label(self):
        label = self.cb_label.get()

        selected_items = self.email_list.selection()

        for item in selected_items:
            try:
                email_id = int(self.email_list.item(item)["values"][0])
            except ValueError:
                email_id = -1

            email_manager.add_label(email_id, label)

        self.get_emails_by_current_user()
