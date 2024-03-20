from flask import *
from app import db
from mongodb import *

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
    movie_names = MongoDB.get_movies(db)
    # cities = [city['city_name'] for city in db.cities.find({}, {'_id': 0, 'city': 1})] # get cities for dropdown list
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(email, password)

    print("Email stored in session:", session.get('email'))  # Debugging statement

    return render_template('home_page.html', movie_names=movie_names, cities=cities)

@home_page.route('/homepage', methods=['GET', 'POST'])
@home_page.route('/home', methods=['GET', 'POST'])
def redirect_homepage():
    return redirect(url_for('home_page.index'))
