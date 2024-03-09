from flask import render_template, redirect, url_for, request, session
from flask import Blueprint
from mongodb import *

# about blueprint definition
sign_in = Blueprint(
    'sign_in',
    __name__,
    static_folder='static',
    static_url_path='/sign_in',
    template_folder='templates'
)


# Routes
@sign_in.route('/sign_in', methods=['GET', 'POST'])
def index():
    return render_template('sign_in.html')

@sign_in.route('/signin')
def redirect_signin():
    return redirect(url_for('sign_in.index'))

