import tkinter as tk
import tkinter.ttk as ttk

from controllers.email import email_manager
from controllers.account import account_manager


class EmailListFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl_greeting = ttk.Label(
            self, text=f"Hello {account_manager.current_user.email} !"
        )
        lbl_greeting.grid(row=0, column=0, padx=5)

        btn_logout = ttk.Button(
            self, text="Logout", command=lambda: controller.show_login_frame()
        )
        btn_logout.grid(row=0, column=1, padx=5)

        self.email_list = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.email_list.grid(row=2, column=0)

        for email in email_manager.get_list(account_manager.current_user.email):
            self.email_list.insert(tk.END, email)

        self.email_list.bind("<<ListboxSelect>>", self.on_select)

    def on_select(self, event):
        selected_indices = self.email_list.curselection()
        selected_items = [self.email_list.get(idx) for idx in selected_indices]
        print("Selected items:", selected_items)
