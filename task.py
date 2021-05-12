from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///task.db"
app.config['SECRET_KEY']= '6dbf57e6dd405d361aa7db16'
db= SQLAlchemy(app)


class User(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    username= db.Column(db.String(length=30), nullable=False, unique=True)
    email_address= db.Column(db.String(length=50), nullable=False, unique=True)
    password= db.Column(db.String(length=60), nullable=False)
    items = db.relationship("Item", backref='owned_user', lazy=True)

class Item(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    task=db.Column(db.String(30), nullable=False, unique=True)
    logs= db.Column(db.String(), nullable=False)
    progress= db.Column(db.String(45), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.task}'



class SignUp(FlaskForm):
    username = StringField(label='username')
    email= StringField(lable='email')
    password1= PasswordField(lable='password1')
    passwoord2= PasswordField(lable='password2')
    submit = SubmitField(lable='submit')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html")


@app.route('/status')
def status_update():
    items= Item.query.all()
    return render_template('status.html', items=items)

    

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/signup')
def sign_up():
    return render_template("sign.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")


if __name__== "__main__":
    app.run(debug=True)