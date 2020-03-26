from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from app.extensions import db, login


## Database model for registered user information
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    ## Store password hashes only, not password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


## Database model for mask inventory information
class Mask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authority = db.Column(db.String(140))
    brand = db.Column(db.String(140))
    size = db.Column(db.String(140))
    number = db.Column(db.Integer)
    item_number = db.Column(db.String(140))
    daily_use = db.Column(db.Integer)
    projected_daily_use = db.Column(db.Integer)
    projected_run_out = db.Column(db.String(64))
    comments = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Mask {}>'.format(self.number)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
