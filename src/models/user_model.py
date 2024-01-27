from db import db
from src.services.user import User

class UserModel(db.Model, User):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))

    def __init__(self, user: User) -> None:
        super().__init__()
        self.id = user.id
        self.map_fields(user)


    def map_fields(self, user: User) -> None:
        self.email = user.email
        self.username = user.username
        self.firstName = user.firstName
        self.lastName = user.lastName