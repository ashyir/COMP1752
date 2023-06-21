from models.email import Email
from models.account import Account, Gender

from controllers.email import email_manager
from controllers.account import account_manager


class Seed:
    def populate(self):
        self.populate_account()
        self.populate_email()

    def populate_account(self):
        for number in range(1, 4):
            account_manager.create_account(
                Account(
                    email=f"tester_0{number}@test.com",
                    password="P@ssword",
                    display_name=f"Tester 0{number}",
                    first_name="Tester",
                    last_name=f"0{number}",
                    birthday="01/01/2000",
                    gender=Gender.Female if number % 2 == 0 else Gender.Male,
                )
            )

    def populate_email(self):
        number = 1

        for sender in account_manager.accounts:
            for recipient in account_manager.accounts:
                email_manager.send_email(
                    Email(
                        sender=sender,
                        recipient=recipient,
                        subject=f"Testing Email {number}",
                        content=f"This is a testing email {number}.",
                        priority=0,
                    )
                )

                number += 1
