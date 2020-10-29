import os
import boto3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
#from config import S3_BUCKET, S3_KEY, S3_SECRET
#from filter import datetimeformat, file_type
#from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import timedelta


#region Configurations  -------- wsgi_app = app.wsgi_app
app = Flask(__name__) # an instantiated Flask variable is contained in the application variable 
app.config['SECRET_KEY'] = 'cg2c29e01302dd66fafae953bcc8f3902' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#app.permanent_session_lifetime = timedelta(day=10)
db = SQLAlchemy(app)
#migrate = Migrate(app, db)

bcrypt = Bcrypt(app) # passing the app to initialise this class

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
 
Bootstrap(app)

#app.jinja_env.filters['datetimeformat'] = datetimeformat
#app.jinja_env.filters['file_type'] = file_type
#endregion

#region Avoiding-Circular-Importing
from application import routes
#endregion