from flask import *
from database import *

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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if checkUsersignin(email, password):
            session['email'] = email
            session.modified = True
            return redirect(url_for('home_page.index'))
        else:
            flash('Invalid email or password')
    return render_template('sign_in.html')





@sign_in.route('/signin')
def redirect_signin():
    return redirect(url_for('sign_in.index'))

