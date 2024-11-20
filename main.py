import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv(".env")

app = Flask(__name__)

CORS(app,origins=["*"])

import controller.symptoms 