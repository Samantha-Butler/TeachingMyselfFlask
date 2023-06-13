from app import db, Todo

first_todo = Todo(todo_text="Learn Flask")   #Storing in Todo within the database
db.session.add(first_todo)
db.session.commit()