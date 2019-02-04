import os
import sys
from flask import Flask
from jinja2.ext import Extension
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
#from Dinero.models import db
from sqlalchemy import create_engine
engine= create_engine('postgresql://abiona_daphne@localhost:5000/expense_sharing')

app = Flask(__name__)
app.config.from_object("config")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\expense_sharing.db'
db = SQLAlchemy(app)
moment = Moment(app)

#mode is either dev or empty
try:
    mode = sys.argv[1]
except:
    mode = None
if mode == "dev":
    #makes the host the localhost when run with "dev"
    app.config["HOST"] = app.config["LOCALHOST"]

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://' + app.config["USERNAME"] + ':' +\
                          app.config["PASSWORD"] + '@' + app.config["HOST"] + ':3306/' + app.config["DB_NAME"]

# Setup SQLAlchemy:
db.init_app(app)

import Dinero.views