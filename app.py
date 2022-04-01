from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)