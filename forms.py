from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Optional
from app.models import User


## Form to gather inventory data about N95 Masks
class MaskForm(FlaskForm):
    brand_options = [('3M', '3M'), ('Moldex', 'Moldex'), ('Other', 'Other')]
    size_options = [('XS', 'Extra small'), ('S', 'Small'), ('M', 'Medium'), ('M/L', 'Medium/Large'), ('L', 'Large'),
                    ('Low Profile', 'Low Profile'), ('Regular', 'Regular'), ('Other', 'Other')]
    brand = SelectField('Brand', choices=brand_options, validators=[DataRequired()])

    ## Figure out how to make "other" field mandatory if selected as option for "brand"
    other = StringField('Other')
    # other = StringField('Other', validators=[RequiredIf()])

    size = SelectField('Size', choices=size_options, validators=[DataRequired()])
    number = IntegerField('Current number of N95 Masks in selected brand.', validators=[DataRequired()])
    ## item_number = serial number?
    item_number = StringField('Item number of N95 Mask in selected brand.', validators=[DataRequired()])
    daily_use = IntegerField('Current daily use of N95 Mask in selected brand.', validators=[DataRequired()])
    projected_daily_use = IntegerField('Projected daily use of N95 Mask in selected brand.',
                                       validators=[DataRequired()])
    ## Unclear about datatype (is it a date? a week day? a count of days?)
    projected_run_out = StringField('Projected day facility will run out of N95 mask in selected brand.',
                                    validators=[DataRequired()])
    comments = StringField('Other comments or special notes.')
    submit = SubmitField('Submit')


## Form to register users
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


## Form to log in users
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
