from flask import Flask
from flask_pymongo import pymongo
import urllib 
import certifi

client = pymongo.MongoClient("mongodb+srv://elea:" + urllib.parse.quote_plus("P@ssword1234") + "@cluster0.sfdcd.mongodb.net/MyDataBase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.get_database("MyDataBase")
collection = db.movie
