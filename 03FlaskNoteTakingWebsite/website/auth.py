from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__) #Blueprint has URLS defined, define multiple files

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else: 
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required #Decorator that does not let users access this page unless they're logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4: #if email is less than 4, issue prompted
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2: #if name is 1 or 0 characters, issue prompted
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2: #if passwords don't match, issue prompted
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7 : #if pass1 is less than 7 characters, issue prompted
            flash('Password must be atleast 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256')) #define fields in modes.py
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True) #Login after creating the acc
            flash('Account created!', category='success')
            return redirect(url_for('views.home')) #Blueprint and function name


    return render_template("sign_up.html", user=current_user)