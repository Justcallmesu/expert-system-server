import os
from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

load_dotenv(".env")

app = Flask(__name__)

CORS(app,origins=["http://localhost:5173"])

client = MongoClient('localhost', 27017)

db = client["expert-system"]

import controller.symptoms 