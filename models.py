import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    name = db.Column(db.String())
    password = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
