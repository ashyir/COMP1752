import tkinter as tk

from models.account import LoginStatus
from controllers.account import account_manager


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0)

        self.lbl_email = tk.Label(self.frame, text="Email")
        self.lbl_email.grid(row=0, column=0, sticky="w")

        self.txt_email = tk.Entry(self.frame, width=50)
        self.txt_email.bind("<Return>", self.on_enter)
        self.txt_email.grid(row=0, column=1, padx=10, pady=5)
        self.txt_email.focus()

        self.lbl_password = tk.Label(self.frame, text="Password")
        self.lbl_password.grid(row=1, column=0, sticky="w")

        self.txt_password = tk.Entry(self.frame, width=50)
        self.txt_password.bind("<Return>", self.on_enter)
        self.txt_password.grid(row=1, column=1, padx=10, pady=5)

        # Create login and cancel buttons in a centered frame.
        btn_frame = tk.Frame(self.frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_cancel = tk.Button(btn_frame, text="Cancel", command=exit)
        self.btn_cancel.pack(side="left", padx=5)

        self.btn_login = tk.Button(btn_frame, text="Login", command=self.login)
        self.btn_login.pack(side="left", padx=5)

        self.lbl_result = tk.Label(self.frame, text="")
        self.lbl_result.grid(row=3, column=0, columnspan=2, pady=5)

        # Display sample accounts.
        self.show_sample_accounts()

    def on_enter(self, event):
        self.login()

    def login(self):
        email = self.txt_email.get()
        password = self.txt_password.get()

        if email == "" or password == "":
            return self.lbl_result.configure(text="Input cannot be blank.")

        # Authenticate user.
        status = account_manager.authenticate(email, password)

        if status == LoginStatus.SUCCESS:
            account = account_manager.get_account(email)
            account_manager.current_user = account

            return self.controller.show_email_list_frame(True)

        if status == LoginStatus.USER_NOT_FOUND:
            return self.lbl_result.configure(text="User does not exist.")

        if status == LoginStatus.WRONG_PASSWORD:
            return self.lbl_result.configure(text="Wrong password.")

    def show_sample_accounts(self):
        accounts = list(account_manager.accounts.values())

        self.txt_email.insert(0, accounts[0].email)
        self.txt_password.insert(0, accounts[0].password)

        for index, account in enumerate(accounts):
            account_frame = tk.Frame(self.frame)
            account_frame.grid(row=4 + index, column=0, columnspan=2, pady=5)

            sample_email = tk.Entry(account_frame, width=25, justify=tk.CENTER)
            sample_email.insert(0, account.email)
            sample_email.pack(side="left", padx=5)
            sample_email.configure(state="readonly")

            sample_password = tk.Entry(account_frame, width=25, justify=tk.CENTER)
            sample_password.insert(0, account.password)
            sample_password.pack(side="left", padx=5)
            sample_password.configure(state="readonly")
