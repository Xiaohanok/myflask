from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def hello():
    return "Hello, Flask!"

@main.route('/index')
def home():
    return render_template('index.html', title="Flask Test Page")