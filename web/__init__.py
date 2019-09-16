import os
from flask import Flask
from flask_pymongo import PyMongo

db = PyMongo()

def init_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.environ.get("DB")
    db.init_app(app)
    
    return app