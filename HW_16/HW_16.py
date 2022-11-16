from flask import Flask

app = Flask


@app.route('/')
def welcome():
    return 'Welcome!'


@app.route('/acquaintance')
def name():
    return 'My name is Liza!'
