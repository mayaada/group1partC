from flask import render_template, redirect, url_for
from flask import Blueprint

# about blueprint definition
movie_screenings = Blueprint(
    'movie_screenings',
    __name__,
    static_folder='static',
    static_url_path='/movie_screenings',
    template_folder='templates'
)


# Routes
@movie_screenings.route('/movie_screenings')
def index():
    return render_template('movie_screenings.html')
