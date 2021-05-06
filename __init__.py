from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from datetime import datetime, timedelta
from DailyLogs import routes
app = Flask(__name__, template_folder='templates')
db= SQLAlchemy(app)
conn = sql.connect('database.db')

