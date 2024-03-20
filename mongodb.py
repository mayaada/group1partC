from datetime import datetime
import random
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import *
from app import *

uri = "mongodb+srv://tamaryos:Tyh0526309028@cluster0.y08h232.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


class MongoDB:
    def __init__(self):
        self.theatres_list = None
        self.screenings_list = None
        self.cities_list = None
        self.users_list = None
        self.movies_list = None
        self.seats = None
        self.cities = None
        self.theatres = None
        self.screenings = None
        self.users = None
        self.movies = None
        client = MongoClient(uri, server_api=ServerApi('1'), tlsInsecure=True)

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        existing_databases = client.list_database_names()

        # #empty database
        # for database_name in existing_databases:
        #     client.drop_database(database_name)

        # Check if the database does not exist
        if 'showtime' not in existing_databases:
            showtime_db = client['showtime']
            self.fill_db(showtime_db)

    def empty_db(self):
        # Remove all documents from each collection
        self.movies.delete_many({})
        self.users.delete_many({})
        self.cities.delete_many({})
        self.theatres.delete_many({})
        self.screenings.delete_many({})

        print("Database emptied successfully.")

    def fill_db(self, db):
        self.movies = db['movies']
        self.users = db['users']
        self.screenings = db['screenings']
        self.theatres = db['theatres']
        self.cities = db['cities']
        self.seats = db['seats']
        self.movies_list = [
            {
                "name": "Barbie",
                "description": "Barbie and Ken are having the time of their lives in the colorful and seemingly "
                               "perfect world of Barbie Land. However, when they get a chance to go to the real "
                               "world, they soon discover the joys and perils of living among humans.",
                "genre": "Comedy",
                "movie_length": "1h 54m",
                "language": "English"
            },
            {
                "name": "Heart of Stone",
                "description": "An intelligence operative for a shadowy global peacekeeping agency races to stop a "
                               "hacker from stealing its most valuable and dangerous weapon.",
                "genre": "Action",
                "movie_length": "2h 2m",
                "language": "English"
            },
            {
                "name": "Oppenheimer",
                "description": "The story of American scientist J. Robert Oppenheimer and his role in the development "
                               "of the atomic bomb.",
                "genre": "Drama",
                "movie_length": "3h",
                "language": "English"
            },
            {
                "name": "The Little Mermaid",
                "description": "A young mermaid makes a deal with a sea witch to trade her beautiful voice for human "
                               "legs so she can discover the world above water and impress a prince.",
                "genre": "Adventure",
                "movie_length": "2h 15m",
                "language": "Hebrew"
            },
            {
                "name": "Fast X",
                "description": "Description for Movie 3",
                "genre": "Drama",
                "movie_length": "2 hours 30 minutes",
                "language": "English"
            },
            {
                "name": "Indiana Jones and the Dial of Destiny",
                "description": "Archaeologist Indiana Jones races against time to retrieve a legendary artifact that "
                               "can change the course of history.",
                "genre": "Action",
                "movie_length": "2h 34m",
                "language": "English"
            }
        ]
        self.users_list = [
            {
                "email": "tamar@gmail.com",
                "password": "password12345"
            },
            {
                "email": "maya@gmail.com",
                "password": "12345678"
            },
            {
                "email": "david@gmail.com",
                "password": "12345678"
            },
            {
                "email": "joni@gmail.com",
                "password": "12345678"
            }
        ]
        self.cities_list = [
            {"city": "Tel Aviv"},
            {"city": "Be'er Sheva"},
            {"city": "Ashdod"},
            {"city": "Haifa"},
            {"city": "Hadera"}
        ]
        self.theatres_list = [
            {
                "theatre": "Yes Planet",
                "city": "Tel Aviv"
            },
            {
                "theatre": "Cinema City",
                "city": "Tel Aviv"
            },
            {
                "theatre": "Yes Planet",
                "city": "Be'er Sheva"
            },
            {
                "theatre": "Cinema City",
                "city": "Be'er Sheva"
            },
            {
                "theatre": "Yes Planet",
                "city": "Ashdod"
            },
            {
                "theatre": "Cinema City",
                "city": "Ashdod"
            },
            {
                "theatre": "Yes Planet",
                "city": "Haifa",
            },
            {
                "theatre": "Cinema City",
                "city": "Haifa",
            },
            {
                "theatre": "Yes Planet",
                "city": "Hadera"

            },
            {
                "theatre": "Cinema City",
                "city": "Hadera"
            }
        ]

        self.screenings_list = self.generate_movie_screenings(self.cities_list, self.movies_list, self.theatres_list)
        self.movies.insert_many(self.movies_list)
        self.users.insert_many(self.users_list)
        self.cities.insert_many(self.cities_list)
        self.theatres.insert_many(self.theatres_list)
        self.screenings.insert_many(self.screenings_list)

    # Define function to generate random screening times
    def generate_screening_times(self):
        times = []
        for i in range(5):
            hour = random.randint(10, 22)  # Random hour between 10 and 22 (10:00 AM to 10:00 PM)
            minute = random.choice([0, 15, 30, 45])  # Random minute (0, 15, 30, or 45)
            times.append(f"{hour:02d}:{minute:02d}")
        return times

    # function to generate random movie screenings for all movies available
    def generate_movie_screenings(self, cities_list, movies_list, theatres_list):
        screenings_list = []
        for movie in movies_list:
            for theatre in theatres_list:
                if theatre["city"] in [city["city"] for city in cities_list]:
                    screening_dates = [datetime(2024, 4, day) for day in range(1, 31)]  # Generate dates for April 2024
                    for date in screening_dates:
                        times = self.generate_screening_times()
                        for time in times:
                            screening = {
                                "movie_name": movie["name"],
                                "date": date.strftime("%m/%d/%y"),
                                "time": time,
                                "theatre": theatre["theatre"],
                                "city": theatre["city"]
                            }
                            screenings_list.append(screening)
        return screenings_list

    # user functions

    def signin(self, email, password):
        # check if the user exists
        user = self.users.find_one({'email': email})
        if user == None:
            return "user", False
        # check if the password is correct
        if user['password'] != password:
            return "password", False
        return 'True', True

        # get user details

        def get_signedin_user(self):
            return self.users.find_one({'email': session['email']})

        # movie search

        def search_movie(self, date, movie_name, city, start_time, end_time):
            return self.movies.find_one({''})

    # Function to retrieve m    ovies from MongoDB
    def get_movies(self):
        movies_collection = self.client['movies']  # Replace with your actual collection name for movies
        movie_names = [movie['movie_name'] for movie in movies_collection.find({}, {'_id': 0, 'movie_name': 1})]  # get movies for dropdown list
        return movie_names

    # Function to retrieve cities from MongoDB
    def get_cities(self):
        cities_collection = db['cities']  # Replace with your actual collection name for cities
        cities = [city['name'] for city in cities_collection.find({}, {'_id': 0, 'cities': 1})]  # Retrieve only city names
        return cities

    def search_movies(self, date, movie_name, city, start_time, end_time):
        pipeline = [
            {"$match": {
                "date": date,
                "movie_name": movie_name,
                "city": city,
                "start_time": {"$gte": start_time},
                "end_time": {"$lte": end_time}
            }}
        ]

        # Execute the aggregation pipeline and retrieve available screenings
        available_screenings = list(self.client.aggregate(pipeline))
        return available_screenings

