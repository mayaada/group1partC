from flask import render_template, redirect, url_for
from flask import Blueprint

# about blueprint definition
home_page = Blueprint(
    'home_page',
    __name__,
    static_folder='static',
    static_url_path='/home_page',
    template_folder='templates'
)


# Routes
@home_page.route('/')
def index():
    return render_template('home_page.html')

@home_page.route('/homepage')
@home_page.route('/home')
def redirect_homepage():
    return redirect(url_for('home_page.index'))

