from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_rating_choices = ("✘",
                         "☕️",
                         "☕️" * 2,
                         "☕️" * 3,
                         "☕️" * 4,
                         "☕️" * 5)

wifi_rating_choices = ("✘",
                       "💪",
                       "💪" * 2,
                       "💪" * 3,
                       "💪" * 4,
                       "💪" * 5)

power_outlet_rating_choices = ("✘",
                               "🔌",
                               "🔌" * 2,
                               "🔌" * 3,
                               "🔌" * 4,
                               "🔌" * 5)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    cafe_location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired()], choices=coffee_rating_choices)
    wifi_rating = SelectField('Wi-Fi Strength Rating', validators=[DataRequired()], choices=wifi_rating_choices)
    power_outlet_rating = SelectField('Power Outlet Availability', validators=[DataRequired()],
                                      choices=power_outlet_rating_choices)
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
        print("True")

        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
