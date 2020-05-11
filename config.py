from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY' ] = 'Secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Arseny\\flask\\flask_app\\database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
