from flask import request
from flask_restful import Resource
from flask import jsonify

from ..services import game_service as service

class Game(Resource):

    def put(self):
        name = request.form["name"]
        env_id = request.form["env_id"]
        due_date = request.form["due_date"]
        num_of_episodes = request.form["num_of_episodes"]

        inserted_id = service.insert_game(name, env_id, due_date, num_of_episodes)

        return jsonify({ "inserted_id": inserted_id })

    def get(self, game_id):
        game = service.find_game(game_id)

        return jsonify(game)

class Games(Resource):
    def get(self):
        games = service.find_all_games()
        
        return jsonify(games)
