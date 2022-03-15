from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

from app.controllers.service_controller import *
load_dotenv('.env')

