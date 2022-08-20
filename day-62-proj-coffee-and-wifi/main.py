from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.fields.html5 import TimeField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_choices = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
wifi_choices = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
power_choices = ['✘', '⚡', '⚡⚡', '⚡⚡⚡', '⚡⚡⚡⚡', '⚡⚡⚡⚡⚡']
time_choices = []


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = TimeField('Opens At', validators=[DataRequired(), InputRequired()])
    close_time = TimeField('Closes At', validators=[DataRequired(), InputRequired()])
    coffee = SelectField('Coffee Rating', choices=coffee_choices, validators=[DataRequired()])
    wifi = SelectField('Wi-Fi Strength', choices=wifi_choices, validators=[DataRequired()])
    power = SelectField('Power Outlet Availability', choices=power_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [form.cafe.data, form.location.data, form.open_time.data,
                   form.close_time.data, form.coffee.data, form.wifi.data, form.power.data]
        with open('cafe-data.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
