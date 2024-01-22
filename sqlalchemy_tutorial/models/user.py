from sqlalchemy_tutorial.models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)


    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email


    def __repr__(self):
        return '<User %r>' % self.username


    def get_all():
        return User.query.all()