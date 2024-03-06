from flask import request
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
@home_page.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(email, password)
    return render_template('home_page.html')

@home_page.route('/homepage', methods=['GET', 'POST'])
@home_page.route('/home', methods=['GET', 'POST'])
def redirect_homepage():
    return redirect(url_for('home_page.index'))

