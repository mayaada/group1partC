from flask import *

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
        # Check if email and password are valid
        if email_valid(email) and password_valid(password):
            session['email'] = email
            session.modified = True
            # print("Email stored in session:", session['email'])  # Debugging statement
            return redirect(url_for('home_page.index'))
        else:
            flash('Invalid email or password')
    return render_template('sign_in.html')


def email_valid(email):
    # Check if the email is not empty and has a valid format
    return email and '@' in email

def password_valid(password):
    # Check if the password is not empty and meets certain criteria
    return password and len(password) >= 6


@sign_in.route('/signin')
def redirect_signin():
    return redirect(url_for('sign_in.index'))

