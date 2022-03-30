from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, Label
from flask_wtf.file import FileField, FileRequired


class AddForm(FlaskForm):
    product_name = StringField('Product name', [InputRequired()])
    product_price = StringField('Product price, e.g. 318 $', [InputRequired()])
    category = SelectField('Category', choices=[('chairs', 'chairs'), ('beds', 'beds'),
                                                ('accessories', 'accessories'), ('furniture', 'furniture'),
                                                ('home_deco', 'home_deco'),
                                                ('dressings', 'dressings'), ('tables', 'tables')])
    description = StringField('Description', [InputRequired()])
    img_url1 = FileField('Product image url 1. view', [FileRequired()])
    img_url2 = FileField('Product image url 2. view', [FileRequired()])
    img_url3 = FileField('Product image url 3. view', [FileRequired()])
    img_url4 = FileField('Product image url 4. view', [FileRequired()])
    quantity = IntegerField('Quantity', [InputRequired()])
    price_id = StringField('Price ID', [InputRequired()])
    submit = SubmitField(label='Submit')


class EditForm(FlaskForm):
    product_name = StringField('Product name', [InputRequired()])
    product_price = StringField('Product price, e.g. 318 $', [InputRequired()])
    category = SelectField('Category', choices=[('chairs', 'chairs'), ('beds', 'beds'),
                                                ('accessories', 'accessories'), ('furniture', 'furniture'),
                                                ('home_deco', 'home_deco'),
                                                ('dressings', 'dressings'), ('tables', 'tables')])
    description = StringField('Description', [InputRequired()])
    img_url1 = StringField('Product image url 1. view', [InputRequired()])
    img_url2 = StringField('Product image url 2. view', [InputRequired()])
    img_url3 = StringField('Product image url 3. view', [InputRequired()])
    img_url4 = StringField('Product image url 4. view', [InputRequired()])
    quantity = IntegerField('Quantity', [InputRequired()])
    price_id = StringField('Price ID', [InputRequired()])
    submit = SubmitField(label='Submit')


class LoginRegisterForm(FlaskForm):
    email = StringField('Please type your e-mail address', [Email()])
    submit = SubmitField(label='Continue')


class LoginForm(FlaskForm):
    email = StringField('Please type your e-mail address', [Email()], render_kw={'readonly': True})
    password = PasswordField('Password', [InputRequired(), Length(min=8)])
    submit = SubmitField(label='Login')


class RegisterForm(FlaskForm):
    email = StringField('Please type your e-mail address', [Email()], render_kw={'readonly': True})
    password = PasswordField('Password', [InputRequired(), Length(min=8)])
    password_check = PasswordField('Type your password again', [InputRequired(), Length(min=8)])
    submit = SubmitField(label='Register')
