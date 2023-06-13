from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy    #Class to interact with database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' # ORM
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/frenz/Desktop/Sam/Python/Flask/02_Flaskwithdb/myapp/myDB.db' # this worked
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # Linking db with app on line 6

#todos = ["Learn Flask", "Set up venv", "Build a cool app"] #Array 

class Todo(db.Model): #Defines what it looks like in the DB and how to acess
    id = db.Column(db.Integer, primary_key = True)
    todo_text = db.Column(db.String(100), index = True)

class TodoForm(FlaskForm):
    todo = StringField("Todo")
    submit = SubmitField("Add Todo")

# with app.app_context():
#     db.create_all() #Runs database code

@app.route('/', methods=["GET", "POST"])
def index(): #Have this Index file match HTML file 
    if 'todo' in request.form: #If a post request is made and has 'todo' attiribute, 
        db.session.add(Todo(todo_text=request.form['todo']))
        db.session.commit()
    return render_template('index.html', todos=Todo.query.all(), template_form=TodoForm()) #Pulls from index html file  #setting todos to the variable, links html to this variable in line 8, pass template form