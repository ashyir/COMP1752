import enum


class Label(enum.Enum):
    IMPORTANT = "Important"
    STAR = "Star"


class Email:
    def __init__(
        self,
        sender=None,
        recipient=None,
        subject=None,
        content=None,
        priority=None,
    ):
        self.recipient = recipient
        self.priority = priority
        self.subject = subject
        self.content = content
        self.sender = sender

        self.datetime = ""
        self.labels = []
        self.id = -1

    def add_label(self, label):
        if label not in self.labels:
            self.labels.append(label)

            return True

        return False

    def remove_label(self, label):
        if label in self.labels:
            self.labels.remove(label)

            return True

        return False

    def __str__(self):
        return f"{self.sender} - {self.subject}"
