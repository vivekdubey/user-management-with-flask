import os
import requests
import hashlib

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import User

@app.route('/', methods=['GET'])
def main_app():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index():
    try:
        name = request.form['name']
        email = request.form['email']
        password = hashlib.md5(request.form['password']).hexdigest()
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
    try:
        user = User(
                    name=name,
                    email=email,
                    password=password
        )
        db.session.add(user)
        db.session.commit()
    except:
        print "errors"
    return render_template('confirm.html', name=name, email=email, password=password)

@app.route('/<user>', methods=['GET'])
def get_user(user):
    u = User.query.filter_by(email=user).first()
    return u.name

if __name__ == '__main__':
    app.run()
