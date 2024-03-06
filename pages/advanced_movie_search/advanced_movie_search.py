from flask import render_template
from flask import Blueprint

# about blueprint definition
advanced_movie_search = Blueprint(
    'advanced_movie_search',
    __name__,
    static_folder='static',
    static_url_path='/advanced_movie_search',
    template_folder='templates'
)


# Routes
@advanced_movie_search.route('/advanced_movie_search')
def index():
    return render_template('advanced_movie_search.html')
