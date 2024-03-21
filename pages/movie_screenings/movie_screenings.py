from flask import render_template, redirect, url_for, request
from flask import Blueprint
from mongodb import *
from database import *

# about blueprint definition
movie_screenings = Blueprint(
    'movie_screenings',
    __name__,
    static_folder='static',
    static_url_path='/movie_screenings',
    template_folder='templates'
)


# Routes
# @movie_screenings.route('/movie_screenings')
# def index():
#     return render_template('movie_screenings.html')

@movie_screenings.route('/search')
def search():
    date = format_mongo_date(request.args.get('date'))
    print('date:', date)
    movie_name = request.args.get('movie')
    print('movie_name:', movie_name)
    city = request.args.get('city')
    start_time = request.args.get('startTime')
    end_time = request.args.get('endTime')
    results_list = findScreenings(date, movie_name, city, start_time, end_time)
    for result in results_list:
        result['date'] = unformat_mongo_date(result['date'])
    print(results_list)
    movie_info = getMovieDetails(movie_name)
    description = movie_info[1]
    genre = movie_info[2]
    length = movie_info[3]
    language = movie_info[4]
    return render_template('movie_screenings.html', results=results_list, movie_name = movie_name, description=description, genre=genre, length=length, language=language)