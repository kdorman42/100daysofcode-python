from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Valid email required.")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message='Password must be 8+ characters.')])
    submit = SubmitField('Log In')


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failed'))
    return render_template('login.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/failed')
def failed():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)