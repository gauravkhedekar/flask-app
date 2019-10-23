from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging as logger
from flask_bcrypt import  Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os
logger.basicConfig(level="DEBUG")
flaskAppInstance = Flask(__name__)
flaskAppInstance.config['SECRET_KEY'] = '1234'
flaskAppInstance.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(flaskAppInstance)
bcrypt = Bcrypt(flaskAppInstance)
login_manager = LoginManager(flaskAppInstance)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
flaskAppInstance.config['MAIL_SERVER']= 'smtp.gmail.com'
flaskAppInstance.config['MAIL_PORT'] = 587
flaskAppInstance.config['MAIL_USE_TLS'] = True
flaskAppInstance.config['MAIL_USERNAME'] = 'khedekarg9@gmail.com'
flaskAppInstance.config['MAIL_PASSWORD'] = 'SSlight70'
#flaskAppInstance.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#flaskAppInstance.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(flaskAppInstance)

from app import routes