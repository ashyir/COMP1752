from tkinter import *

from controllers.account import account_manager


class LoginFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = Frame(self)
        self.frame.grid(row=0, column=0)

        self.lbl_email = Label(self.frame, text="Email")
        self.lbl_email.grid(row=0, column=0, sticky="w")

        self.txt_email = Entry(self.frame, width=50)
        self.txt_email.bind("<Return>", self.on_enter)
        self.txt_email.grid(row=0, column=1, padx=10, pady=5)
        self.txt_email.focus()

        self.lbl_password = Label(self.frame, text="Password")
        self.lbl_password.grid(row=1, column=0, sticky="w")

        self.txt_password = Entry(self.frame, width=50)
        self.txt_password.bind("<Return>", self.on_enter)
        self.txt_password.grid(row=1, column=1, padx=10, pady=5)

        # Create login and cancel buttons in a centered frame.
        btn_frame = Frame(self.frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_cancel = Button(btn_frame, text="Cancel", command=exit)
        self.btn_cancel.pack(side="left", padx=5)

        self.btn_login = Button(btn_frame, text="Login", command=self.login)
        self.btn_login.pack(side="left", padx=5)

        self.lbl_result = Label(self.frame, text="")
        self.lbl_result.grid(row=3, column=0, columnspan=2, pady=5)

        # Display sample accounts.
        self.show_sample_accounts()

    def on_enter(self, event):
        self.login()

    def login(self):
        email = self.txt_email.get()
        password = self.txt_password.get()

        # Login success.
        if account_manager.authenticate(email, password):
            account = account_manager.get_account(email)
            account_manager.current_user = account

            return self.controller.show_email_list_frame(True)

        # Login fail.
        return self.lbl_result.configure(text="Login failed.")

    def show_sample_accounts(self):
        accounts = list(account_manager.accounts.values())

        self.txt_email.insert(0, accounts[0].email)
        self.txt_password.insert(0, accounts[0].password)

        for index, account in enumerate(accounts):
            account_frame = Frame(self.frame)
            account_frame.grid(row=4 + index, column=0, columnspan=2, pady=5)

            sample_email = Entry(account_frame, width=25, justify=CENTER)
            sample_email.insert(0, account.email)
            sample_email.pack(side="left", padx=5)
            sample_email.configure(state="readonly")

            sample_password = Entry(account_frame, width=25, justify=CENTER)
            sample_password.insert(0, account.password)
            sample_password.pack(side="left", padx=5)
            sample_password.configure(state="readonly")
