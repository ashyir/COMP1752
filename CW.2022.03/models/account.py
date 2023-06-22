import enum


class Gender(enum.Enum):
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"


class LoginStatus(enum.Enum):
    FAIL = 0
    SUCCESS = 1
    USER_NOT_FOUND = 2
    WRONG_PASSWORD = 3


class Account:
    def __init__(
        self,
        email=None,
        password=None,
        display_name=None,
        first_name=None,
        last_name=None,
        birthday=None,
        gender=None,
    ):
        self.email = email
        self.password = password
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender

    def __str__(self):
        return f"{self.display_name} ({self.email})"
