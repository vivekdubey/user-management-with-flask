import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, email, name, password, is_admin):
        self.email = email
        self.name = name
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<id {}>'.format(self.id)
