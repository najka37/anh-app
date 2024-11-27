from flask import Flask, session
app = Flask(__name__)

from app.public import public_view
from app.users import users_view
from app import configuration

#Set a secret key to the session
app.secret_key = '123'