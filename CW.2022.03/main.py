from ui.window_main import MainWindow

from controllers.email import EmailController
from controllers.account import AccountController

from models.account import Account, Gender

account = Account(
    "admin@test.com",
    "p@ssword",
    "Admin 01",
    "Admin",
    "01",
    "01/01/2000",
    Gender.Female,
)

AccountController.create_account(account)

app = MainWindow()
app.mainloop()
