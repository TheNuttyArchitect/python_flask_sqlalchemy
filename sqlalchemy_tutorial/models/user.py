from ..db_factory import get_db

db = get_db()

class user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(255), unique=True, nullable = False)
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % self.username
    