from flask import Flask, jsonify
from .models import db, user
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = db.db
db.init_app(app)
Migrate(app, db)


@app.route('/users')
def get_users():
    users = user.User.get_all()
    results = []
    for u in users:
        results.append({'id': u.id, 'username': u.username, 'email': u.email})

    return jsonify(results)

if __name__ == '__main__':
    db.init_app()
    app.run()


'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username
'''
