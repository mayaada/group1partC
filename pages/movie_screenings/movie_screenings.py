from flask import *

# about blueprint definition
movie_screenings = Blueprint(
    'movie_screenings',
    __name__,
    static_folder='static',
    static_url_path='/movie_screenings',
    template_folder='templates'
)


# Routes
@movie_screenings.route('/movie_screenings' , methods=['GET', 'POST'])
def index():
    if request.method == 'GET':

        return render_template('movie_screenings.html')
    return render_template('movie_screenings.html')
