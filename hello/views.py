from flask import request

from hello.tasks import add
from flask import render_template, jsonify
import models as dbHandler


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
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('index.html', users=users)
    else:
        return render_template('index.html')
