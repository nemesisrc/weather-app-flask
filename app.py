from flask import Flask, render_template, request
from weather import current_weather

app = Flask(__name__)

@app.route('/')
def index():
    return "this is the main app.py file!!"


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)