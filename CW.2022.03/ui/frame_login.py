import tkinter as tk

from controllers.account import AccountController as accounts


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.btn_cancel = tk.Button(self, text="Cancel", command=exit)
        self.btn_cancel.grid(column=0, row=3)

        self.btn_login = tk.Button(self, text="Login", command=self.login)
        self.btn_login.grid(column=1, row=3)

        self.lbl_email = tk.Label(self, text="Email")
        self.lbl_email.grid(column=0, row=0)

        self.lbl_password = tk.Label(self, text="Password")
        self.lbl_password.grid(column=0, row=1)

        self.txt_email = tk.Entry(self, width=50)
        self.txt_email.grid(column=1, row=0)
        self.txt_email.focus()

        self.txt_password = tk.Entry(self, width=50)
        self.txt_password.grid(column=1, row=1)

        self.lbl_result = tk.Label(self, text="")
        self.lbl_result.grid(column=1, row=4)

    def login(self):
        email = self.txt_email.get()
        password = self.txt_password.get()

        if accounts.authenticate(email, password):
            self.controller.login(True)
        else:
            self.lbl_result.configure(text="Login failed.")
