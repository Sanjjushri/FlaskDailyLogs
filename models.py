from DailyLogs import db
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql

db= SQLAlchemy(app)
conn = sql.connect('database.db')



class Item(db.Model):
  
    id = db.Column(db.Integer, primary_key=True )
    task= db.Column(db.String(100), nullable=False)
    logs = db.Column(db.Integer, nullable=False)
    time=db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    progress= db.Column(db.String(100), nullable=False)
    description= db.Column(db.String(1000), unique=True)

    def __repr__(self):
        return f'Item {self.name}'
