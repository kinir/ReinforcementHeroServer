from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

db = MongoAlchemy()

def init_app():
    app = Flask(__name__)
    db.init_app(app)
    
    return app