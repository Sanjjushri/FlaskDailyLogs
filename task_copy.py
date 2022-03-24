from flask_wtf import Form

# from wtforms import TextField, BooleanField
# from wtforms.validators import Required


from flask import Flask, render_template,  request,redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf import form
# from wtforms.fields.core import IntegerField, StringField
from forms import SignUpForm, DailyLogsForm
from flask import Blueprint

app = Flask(__name__, template_folder='templates')
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///task.db"
# app.config['SECRET_KEY']= '6dbf57e6dd405d361aa7db16'
# db= SQLAlchemy(app)


# class User(db.Model):
#     id= db.Column(db.Integer(), primary_key=True)
#     username= db.Column(db.String(length=30), nullable=False, unique=True)
#     email_address= db.Column(db.String(length=50), nullable=False, unique=True)
#     password= db.Column(db.String(length=60), nullable=False)
#     items = db.relationship("Item", backref='owned_user', lazy=True)

# class Item(db.Model):
#     id= db.Column(db.Integer(), primary_key=True)
#     task=db.Column(db.String(30), nullable=False, unique=True)
#     logs= db.Column(db.String(), nullable=False)
#     progress= db.Column(db.String(45), nullable=False)
#     owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

#     def __repr__(self):
#         return f'Item {self.task}'

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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form= SignUpForm()
    if form.is_submitted():
       result= request.form
       return render_template('status.html', result=result)
    if form.errors != {}: #if there are not errors from the validations
        for err_msg in form.errors.values():
            print(f'There was n error with creating a user: {err_msg}')
    return render_template("signup.html", form = form)

@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/dailylogs', methods=['GET','POST'])
def dailylogs():
    form=  DailyLogsForm()
    if form.is_submitted():
        result= request.form
        return render_template('update.html', result=result)
    return render_template('dailylogs.html', form=form)


if __name__== "__main__":
    app.run(debug=True)