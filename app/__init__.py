from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging as logger
from flask_bcrypt import  Bcrypt
from flask_login import LoginManager

logger.basicConfig(level="DEBUG")
flaskAppInstance = Flask(__name__)
flaskAppInstance.config['SECRET_KEY'] = '1234'
flaskAppInstance.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(flaskAppInstance)
bcrypt = Bcrypt(flaskAppInstance)
login_manager = LoginManager(flaskAppInstance)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes