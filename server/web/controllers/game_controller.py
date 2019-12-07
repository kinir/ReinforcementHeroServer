from flask import request
from flask_restful import Resource
from flask import jsonify

from ..services import game_service as service
from ..services import environment_service as env_service

class Game(Resource):

    def put(self):
        name = request.form["name"]
        env_id = request.form["env_id"]
        due_date = request.form["due_date"]
        num_of_episodes = int(request.form["num_of_episodes"])

        inserted_id = service.insert_game(name, env_id, due_date, num_of_episodes)

        # Get environmnet on which the random agent will run
        env = env_service.find_env(env_id)

        # Generate a random agent and submit as a default agent
        service.submit_random_agent(inserted_id, env.gym_env, num_of_episodes)

        return jsonify({ "inserted_id": inserted_id })

    def get(self, game_id):
        game = service.find_game(game_id)

        return jsonify(game)

class Games(Resource):
    def get(self):
        games = service.find_all_games()
        
        return jsonify(games)
