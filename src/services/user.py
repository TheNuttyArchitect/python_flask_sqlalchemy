class User:
    id: int
    username: str
    email: str
    firstName: str
    lastName: str

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.firstName,
            'lastName': self.lastName
        }