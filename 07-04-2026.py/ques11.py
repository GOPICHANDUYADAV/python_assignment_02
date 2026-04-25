#data valiator with property decorators
class UserProfile:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters")
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise ValueError("Age must be between 0 and 120")
        self._age = value


# Test
user = UserProfile("alice", "alice@example.com", 25)

print(user.username)

user.username = "bob"
print(user.username)