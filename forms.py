from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email , DataRequired

class SignUpForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address= StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6),  DataRequired()])
    password2= PasswordField(label='Confirm Password:', validators=[EqualTo('password1'),  DataRequired()])
    submit = SubmitField(label='Create Account')

class DailyLogsForm(FlaskForm):
    task = StringField(label='Enter Task:', validators=[Length(min=2, max=40), DataRequired()])
    start_time= StringField(label="Start time:", validators=[DataRequired()]) 
    end_time= StringField(label="End time:", validators=[DataRequired()])  
    expenses= IntegerField(label="Expenses in Rupee:", validators=[DataRequired()]) 
    add_task= SubmitField(label='ADD TASK')