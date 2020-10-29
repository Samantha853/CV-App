#region IMPORT

import io
import os
import os.path
import smtplib
import glob
import json
import re
import csv
import math
import time
import boto3
import pandas as pd
from csv import writer
from csv import reader
from random import randrange
from sqlalchemy import update
from sqlalchemy import create_engine
from flask_bootstrap import Bootstrap
from application import app, db, bcrypt
#from config import S3_BUCKET, S3_KEY, S3_SECRET
from application.models import User
from flask import render_template, url_for, flash, redirect, request, session
from werkzeug.exceptions import HTTPException
from application.forms import (RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm)
from flask_login import login_user, current_user, logout_user, login_required
import logging
from logging.handlers import SMTPHandler
import smtplib, ssl
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#endregion

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# log files
login_file_handler = logging.FileHandler('user.log') # LOGIN - FILEHANDLE
ise_file_handler = logging.FileHandler('activity.log') # INTERNAL SERVER ERRORS - FILEHANDLER

ise_file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

login_file_handler.setFormatter(formatter)
ise_file_handler.setFormatter(formatter)

# adding handlers
logger.addHandler(login_file_handler)
logger.addHandler(ise_file_handler)
logger.addHandler(stream_handler)

# LOGIN
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('Register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')
