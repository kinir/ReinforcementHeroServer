from flask import request
from flask_restful import Resource

from ..services import game_service as service

class Game(Resource):
    def put(self):
        game_id = request.form["game_id"]
        game_name = request.form["group_name"]
        env_id = request.form["env_id"]
        due_date = request.form["due_date"]
        num_of_episods = request.form["num_of_episods"]

    def get(self):
        pass