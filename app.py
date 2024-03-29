from flask import *
from mongodb import *
from database import *

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.home_page.home_page import home_page

app.register_blueprint(home_page)


## sign in
from pages.sign_in.sign_in import sign_in

app.register_blueprint(sign_in)

## register
from pages.register.register import register

app.register_blueprint(register)


## advanced_movie_search
from pages.advanced_movie_search.advanced_movie_search import advanced_movie_search

app.register_blueprint(advanced_movie_search)


## contact_us
from pages.contact_us.contact_us import contact_us

app.register_blueprint(contact_us)


## movie_screenings
from pages.movie_screenings.movie_screenings import movie_screenings

app.register_blueprint(movie_screenings)



## order_page
from pages.order_page.order_page import order_page

app.register_blueprint(order_page)

###### Components
## Navar
from components.navbar.navbar import navbar

app.register_blueprint(navbar)


## Footer
from components.footer.footer import footer

app.register_blueprint(footer)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

