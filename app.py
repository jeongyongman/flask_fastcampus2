import os
from flask import Flask
from flask_jwt import JWT
from flask import render_template
from models import Fcuser, db
from api_v1 import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile =  os.path.join(basedir,'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'ddd'

db.init_app(app)
db.app = app
db.create_all()

def authenticate(username, password):
    user = Fcuser.query.filter(Fcuser.userid == username).first()
    if user.password == password:
        return user

jwt = JWT(app, authenticate)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)