from models.account import Account


class AccountController:
    _instance = None

    accounts = {}
    current_user = Account()

    # Singleton.
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def get_account(self, email):
        return self.accounts[email]

    def create_account(self, account):
        if account.email not in self.accounts.keys():
            self.accounts[account.email] = account

            return True

        return False

    def update_account(self, account):
        if account.email in self.accounts.keys():
            self.accounts[account.email] = account

            return True

        return False

    def delete_account(self, email):
        if email in self.accounts.keys():
            del self.accounts[email]

            return True

        return False

    def authenticate(self, email, password):
        if email in self.accounts.keys():
            if self.accounts[email].password == password:
                return True

        return False

    def change_password(self, email, new_password):
        if email in self.accounts.keys():
            self.accounts[email].password = new_password

            return True

        return False


account_manager = AccountController()
