from this import d
from flask import Flask, flash, render_template, redirect, url_for, request
from .forms import LoginForm, RegisterForm
from app import app, db
from werkzeug.security import check_password_hash, generate_password_hash
from .models import UserInfo
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@login_required
def Index():

    name = current_user.username
    return render_template('index.html', name=name)


@app.route('/contact')
def Contact():
    return render_template('contact.html')


@app.route('/about')
def About():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()

    if request.method =='POST':
        if form.validate_on_submit():
            user = UserInfo.query.filter_by(username = form.username.data).first()

            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)

                    return redirect(url_for('Index'))

                flash("Invalid Credentials")
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        username = form.username.data
        password = hashed_password
        email = form.email.data

        new_register = UserInfo(username=username, password=password, email=email)

        db.session.add(new_register)
        db.session.commit()

        flash("Registration was successfull")

        return redirect (url_for('Login'))

    return render_template('registration.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')