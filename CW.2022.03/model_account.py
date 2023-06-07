import enum

class Gender(enum.Enum):
    Female = 0
    Male = 1
    Other = 2
    
class Account:
    def __init__(self, email, password, display_name, first_name, last_name, birthday, gender):
        self.email = email
        self.password = password
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender