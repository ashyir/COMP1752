from datetime import datetime


class EmailController:
    _instance = None

    emails = {}
    current_index = 0

    # Singleton.
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def get_list(self, recipient_email):
        email_list = []

        for email in self.emails.values():
            if email.recipient == recipient_email:
                email_list.append(email)

        return email_list

    def send_email(self, email):
        email.id = self.current_index
        email.datetime = datetime.now()
        self.emails[self.current_index] = email

        self.current_index += 1

    def read_email(self, id):
        try:
            return self.emails[int(id)]
        except Exception:
            return None

    def delete_email(self, id):
        try:
            del self.emails[int(id)]
            return True
        except Exception:
            return False

    def add_label(self, id, label):
        try:
            self.emails[int(id)].add_label(label)
            return True
        except Exception:
            return False

    def remove_label(self, id, label):
        try:
            self.emails[int(id)].remove_label(label)
            return True
        except Exception:
            return False

    def update_priority(self, id, priority):
        try:
            self.emails[int(id)].priority = priority
            return True
        except Exception:
            return False


email_manager = EmailController()
