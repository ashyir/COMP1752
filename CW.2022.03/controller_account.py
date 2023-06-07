class AccountController:
    accounts = {}

    def register(self, account):
        if account.email not in self.accounts.keys():
            self.accounts[account.email] = account

            return True
        
        return False

    def login(self, email, password):
        if self.accounts[email].password == password:
            return True
            
        return False