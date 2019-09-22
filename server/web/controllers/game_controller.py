from flask import request
from flask_restful import Resource

from ..services import game_service as service

class Game(Resource):

    def put(self):
        try:
            game_name = request.form["game_name"]
            env_id = request.form["env_id"]
            due_date = request.form["due_date"]
            num_of_episods = request.form["num_of_episods"]

            service.insert_game(game_name, env_id, due_date, num_of_episods)
        
        except Exception as e:
            return repr(e)

        return True

    def get(self, game_id):
        # Fetch all the record(s)
        game_properties = service.find_game(game_id)
        return game_properties