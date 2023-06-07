class EmailController:
    emails = {}
    current_index = 0

    def show_list(self, recipient_email):
        email_list = []

        for email in self.emails.values():
            if email.recipient == recipient_email:
                email_list.append(email)

        return email_list

    def send_email(self,  email):
        email.update_id(self.current_index)
        self.emails[self.current_index] = email
        
        self.current_index += 1
    
    def delete_email(self, email_id):
        del self.emails[email_id]

    def add_label(self, email_id, label):
        return self.emails[email_id].add_label(label)
    
    def remove_label(self, email_id, label):
        return self.emails[email_id].remove_label(label)