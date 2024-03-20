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

