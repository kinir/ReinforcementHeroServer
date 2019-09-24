from flask import request
from flask_restful import Resource
from flask import jsonify

from ..services import game_service as service

class Game(Resource):

    def put(self):
        try:
            name = request.form["name"]
            env_id = request.form["env_id"]
            due_date = request.form["due_date"]
            num_of_episods = request.form["num_of_episods"]

            service.insert_game(name, env_id, due_date, num_of_episods)
        
        except Exception as e:
            return repr(e)

        return True

    def get(self, game_id=None):
        if(game_id is None):
            all_games = service.find_all_games()
            return jsonify(all_games)
        else:
            game_properties = service.find_game(game_id)
            return jsonify(game_properties)