class User:
    id: int
    username: str
    email: str
    firstName: str
    lastName: str

    def __init__(self, values: dict = None) -> None:
        if values is not None: 
            id = values.get("id")
            if id is not None:
                self.id = int(id)
            self.username = values.get("username")
            self.email = values.get("email")
            self.firstName = values.get("firstName")
            self.lastName = values.get("lastName")

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.firstName,
            'lastName': self.lastName
        }