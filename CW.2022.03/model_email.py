import enum

class Label(enum.Enum):
    Important = 1
    Star = 2
    
class Email:
    id = -1
    labels = []

    def __init__(self, priority, sender, recipient, subject, content):
        self.priority = priority
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.content = content

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

    def update_id(self, id):
        self.id = id