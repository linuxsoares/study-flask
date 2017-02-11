from flask import request

from hello.tasks import add
from flask import render_template, jsonify
from models import User
from database import db_session


def hello_world():
    add.delay(1,2)
    return 'Hello, World!'


def ola():
    add.delay(10, 20)
    return render_template(
        'ola.html',
        results={
            'name': 'Gilmar',
            'old': '35'
        }
    )


def test():
    add.delay(15, 25)
    d = {"message": "Hello World!", 'a': 1}
    return jsonify(**d)


def home():
    add.delay(9,9)
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user = User(name=username, password=password)
        db_session.add(user)
        db_session.commit()
        users = User.query.all()
        return render_template('index.html', users=users)
    else:
        users = User.query.all()
        return render_template('index.html', users=users)
