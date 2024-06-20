from .User import User

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = 'customer'
