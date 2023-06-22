from datetime import datetime

from controllers.account import account_manager


class EmailController:
    _instance = None

    emails = {}
    current_index = 0

    # Singleton.
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def get_emails_by_recipient(self, recipient_email):
        email_list = []

        for email in self.emails.values():
            if email.recipient == recipient_email:
                email_list.append(email)

        return email_list

    def get_emails_by_label(self, label):
        email_list = []

        for email in self.emails.values():
            if label in email.labels:
                email_list.append(email)

        return email_list

    def send_email(self, email):
        if email.recipient not in account_manager.accounts.keys():
            recipient = email.recipient
            email.recipient = email.sender
            email.sender = "no_reply@test.com"
            email.subject = "Email Failure"
            email.content = f"The account '{recipient}' does not exist."

        email.id = self.current_index
        email.datetime = datetime.now()
        self.emails[self.current_index] = email

        self.current_index += 1

    def read_email(self, id):
        if id in self.emails.keys():
            return self.emails[id]

        return None

    def delete_email(self, id):
        if id in self.emails.keys():
            del self.emails[id]

            return True

        return False

    def add_label(self, id, label):
        if id in self.emails.keys():
            self.emails[id].add_label(label)

            return True

        return False

    def remove_label(self, id, label):
        if id in self.emails.keys():
            self.emails[id].remove_label(label)

            return True

        return False

    def update_priority(self, id, priority):
        if id in self.emails.keys():
            self.emails[id].priority = priority

            return True

        return False


# Initialize controller.
email_manager = EmailController()
