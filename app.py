from flask import *

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

# ## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
#
# app.register_blueprint(page_error_handlers)
#
###### Components
## Navar
from components.navbar.navbar import navbar

app.register_blueprint(navbar)


## Footer
from components.footer.footer import footer

app.register_blueprint(footer)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tamaryos:Tyh0526309028@cluster0.y08h232.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
sample_analytics_db = client['sample_analytics']
mydb = client['mydatabase']
customers = mydb['customers']
