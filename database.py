from datetime import datetime
import random
from tkinter import messagebox

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import *
from settings import DB_URI
from app import *

uri = DB_URI
client = MongoClient(uri, server_api=ServerApi('1'), tlsInsecure=True)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

existing_databases = client.list_database_names()
print(existing_databases)

db = client['showtime']
users = db['users']
movies = db['movies']
screenings = db['screenings']
cities = db['cities']

# print all documents in the collection
for doc in users.find():
    print(doc)


    def checkUsersignin(email, password):
        # check if the user exists
        user = users.find_one({'email': email})
        if user is None:
            return False

        # check if the password is correct
        if user['password'] != password:
            return False
        return True

    #check if the user exists
    def checkUser(email , password):
        print("checkUser")
        user = users.find_one({'email': email})
        print("Retrieved user:", user)  # Debugging output
        if user is None:
            print("user is None")
            users.insert_one({'email': email, 'password': password})
            return True
        return False


    def findScreenings(date, movie_name, city, start_time, end_time):
        print("findScreenings")
        screenings_list = []
        print("Searching for screenings:", movie_name, date, city, start_time, end_time)
        cursor = screenings.find({
            'movie_name': movie_name,
            'date': date,
            'time': {'$gte': start_time, '$lte': end_time},
            'city': city
        }).sort('time', pymongo.ASCENDING)

        for screening in cursor:
            screenings_list.append(screening)

        if not screenings_list:
            print("No screenings available for this time period. Please try a different date or time.")

        return screenings_list


    def getMovieDetails(movie_name):
        print("getMovieDetails")
        print("Searching for movie:", movie_name)
        movie = movies.find_one({'name': movie_name})
        print("Found movie:", movie)
        if movie is None:
            print("Movie not found")
            return None, None, None, None, None
        else:
            description = movie.get('description')
            genre = movie.get('genre')
            length = movie.get('movie_length')
            language = movie.get('language')
            return movie, description, genre, length, language

    # create a function that formats my string variable which looks like yyyyy-mm-dd to mm/dd/yy
    def format_mongo_date(date):
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%m/%d/%y")
        return date

    #create a function that formats my formated date to dd-mm-yyyyy
    def unformat_mongo_date(date):
        date = datetime.strptime(date, "%m/%d/%y")
        date = date.strftime("%d-%m-%Y")
        return date



    # def search_movies(self, date, movie_name, city, start_time, end_time):
    #     pipeline = [
    #         {"$match": {
    #             "date": date,
    #             "movie_name": movie_name,
    #             "city": city,
    #             "start_time": {"$gte": start_time},
    #             "end_time": {"$lte": end_time}
    #         }}
    #     ]
    #
    #     # Execute the aggregation pipeline and retrieve available screenings
    #     available_screenings = list(self.client.aggregate(pipeline))
    #     return available_screenings

