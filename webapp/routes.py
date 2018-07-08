"""

copyright: Sergio M. Santos, Univ. of Aveiro, Portugal, 2018

"""

__author__ = "Sergio M. Santos"
__status__ = "Development"
__version__ = "0.1"

from flask import render_template
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
