import tkinter as tk


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.btn_cancel = tk.Button(self, text="Cancel", command=exit)
        self.btn_cancel.grid(column=0, row=3)

        self.btn_login = tk.Button(self, text="Login", command=self.login)
        self.btn_login.grid(column=1, row=3)

        self.lbl_username = tk.Label(self, text="Username")
        self.lbl_username.grid(column=0, row=0)

        self.lbl_password = tk.Label(self, text="Password")
        self.lbl_password.grid(column=0, row=1)

        self.txt_username = tk.Entry(self, width=50)
        self.txt_username.grid(column=1, row=0)
        self.txt_username.focus()

        self.txt_password = tk.Entry(self, width=50)
        self.txt_password.grid(column=1, row=1)

        self.lbl_result = tk.Label(self, text="")
        self.lbl_result.grid(column=1, row=4)

    def login(self):
        username = self.txt_username.get()
        password = self.txt_password.get()

        if username == "admin" and password == "admin":
            self.controller.login(True)
        else:
            self.lbl_result.configure(text="Login failed.")
