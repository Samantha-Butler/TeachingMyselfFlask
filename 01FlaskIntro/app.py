from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

gratitudes = ["Learn Flask", "Set up venv"]

class GratitudeForm(FlaskForm):
    gratitude = StringField("What gratitude would you like to add?") #Label before text field
    submit = SubmitField("Add gratitude") #Label on submit button

@app.route('/', methods=["GET", "POST"]) 
def index():
    if 'gratitude' in request.form:
        gratitudes.append(request.form['gratitude'])
    return render_template('index.html', gratitudes=gratitudes, template_form=GratitudeForm())