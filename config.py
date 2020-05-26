from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Testing App')
    parser.add_argument('db', type=str, nargs='?', default='5000')
    parser.add_argument('port', type=int, nargs='?', default=5000)
    parser.add_argument('host', type=str, nargs='?', default='localhost')
    return parser.parse_args()


args = parse_args()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + args.db
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
