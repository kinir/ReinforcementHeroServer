import base64
from datetime import datetime
import os

from bson.objectid import ObjectId
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

from .error_handler import handle_exception
from .models.environment_model import Environment
from .models.game_model import Game
from .models.submission_model import Submission

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S")
        elif isinstance(obj, Game) or isinstance(obj, Submission) or isinstance(obj, Environment):
            return obj.to_dict()
            
        return JSONEncoder.default(self, obj)

db = PyMongo()

def init_app():
    app = Flask(__name__)
    app.register_error_handler(Exception, handle_exception)

    # Enable cross origin access
    CORS(app)

    app.json_encoder = CustomJSONEncoder
    app.config["MONGO_URI"] = os.environ.get("DB")
    db.init_app(app)
    
    return app
