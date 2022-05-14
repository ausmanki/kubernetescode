from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'demo brasileg thank you'
    return 'ok'
