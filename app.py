from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

serve(app, host='0.0.0.0', port=8000)
