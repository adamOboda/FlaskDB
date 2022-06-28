from app import db, login_manager
from flask_login import UserMixin


class UserInfo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


@login_manager.user_loader
def load_user(user_id):
    return UserInfo.query.get(int(user_id))
