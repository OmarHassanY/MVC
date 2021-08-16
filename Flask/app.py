from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'OMMMMMMMMMMMMMMAR Hassan'


@app.route('/register/<int:number>')
def register(number=0):
    return render_template('register.html', number=number)
