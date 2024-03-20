from flask import *
from database import *
# about blueprint definition
register = Blueprint(
    'register',
    __name__,
    static_folder='static',
    static_url_path='/register',
    template_folder='templates'
)


# Routes
@register.route('/register' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('password')
        if checkUser(email, password):
            session['email'] = email
            session.modified = True
            return redirect(url_for('home_page.index'))
        else:
            flash('user already exists')
    return render_template('register.html')
