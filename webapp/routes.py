"""

copyright: Sergio M. Santos, Univ. of Aveiro, Portugal, 2018

"""

__author__ = "Sergio M. Santos"
__status__ = "Development"
__version__ = "0.1"

from flask import render_template, render_template_string
from flask import request, url_for, redirect
from flask import Flask, Response, make_response
from flask import Markup, flash

# from dataflow.forms import RegistrationForm, LoginForm
# from dataflow.utils import list_available_modules
# from dataflow import app, db, mongo
# from dataflow.models import User

# from werkzeug.urls import url_parse
# import flask_login 


from webapp import app

#------------------------------------------------------------------------------

@app.route('/')
def index():
    '''
    Main entry point to the application
    '''
    return render_template('index.html')


@app.route('/login')
def login():
    '''
    Main entry point to the application
    '''
    return render_template('login.html')


@app.route('/register')
def register():
    '''
    Main entry point to the application
    '''
    return render_template('register.html')

@app.route('/market')
def market():
    '''
    Main entry point to the application
    '''
    return render_template('market.html')

@app.route('/rentals')
def rentals():
    '''
    Main entry point to the application
    '''
    return render_template('rentals.html')


@app.route('/houses')
def houses():
    return render_template('houses.html')


# #------------------------------------------------------------------------------

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     '''
#     Registration endpoint via HTML forms
#     '''
#     if flask_login.current_user.is_authenticated:
#         return redirect(url_for('home'))
    
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('home'))
    
#     return render_template('register.html', title='Register', form=form)

# #------------------------------------------------------------------------------

# @app.route('/home')
# @flask_login.login_required
# def home():
#     '''
#     Main entry point to the application.
#     The template is rendered and a CSRF token
#     is appended to prevent cross-site request forgery attacks.
#     '''
#     user = flask_login.current_user

#     modules = list_available_modules()
#     includes = [Markup("{%% include '%s.html' %%}") % m for m in modules]
#     # documents = ['document-%d'%n for n in range(5)]

#     documents = list(mongo.db.documents.find({'owner': user.get_id()}))
#     # print documents

#     template = render_template(
#         'composer.html',
#         modules=modules,
#         includes=includes,
#         documents=documents,
#         user=user)
    
#     return render_template_string(template)

# #------------------------------------------------------------------------------

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     '''
#     Login endpoint via HTML form
#     '''
#     if flask_login.current_user.is_authenticated:
#         return redirect(url_for('home'))
    
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()

#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
        
#         flask_login.login_user(user)#, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('home')
#         return redirect(next_page)
    
#     return render_template('login.html', form=form)
    
# #------------------------------------------------------------------------------

# @app.route('/logout')
# def logout():
#     '''
#     Logout endpoint
#     '''
#     flask_login.logout_user()
#     return redirect(url_for('index'))

# #------------------------------------------------------------------------------

# @app.route('/pairdist')
# def redirect_dash():
#     return redirect('/dash')