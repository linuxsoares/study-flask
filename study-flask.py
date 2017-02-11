from flask import Flask

from database import init_db
from hello.views import hello_world, ola, test, home

app = Flask(__name__)

app.add_url_rule('/', 'hello_world', hello_world)
app.add_url_rule('/ola', 'ola', ola)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/home', 'home', home, methods=['GET', 'POST'])

init_db()
app.run()
