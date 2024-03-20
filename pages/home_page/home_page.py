from flask import *
from database import *

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
    movies_col = movies.find({'name': {'$exists': True}}).sort('name', pymongo.ASCENDING)
    movie_names = [movie['name'] for movie in movies_col]
    cities_col = cities.find({'city': {'$exists': True}}).sort('city', pymongo.ASCENDING)
    city_names = [city['city'] for city in cities_col]
    return render_template('home_page.html', movies=movie_names , cities=city_names)


@home_page.route('/homepage', methods=['GET', 'POST'])
@home_page.route('/home', methods=['GET', 'POST'])
def redirect_homepage():
    return redirect(url_for('home_page.index'))
