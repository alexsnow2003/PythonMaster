class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = 'user'

    def get_role(self):
        return self.role
