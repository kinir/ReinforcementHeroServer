from flask import request
from flask_restful import Resource
from flask import jsonify

from ..services import submission_service as service
from ..services import environment_service
from ..services import game_service

class Submission(Resource):
    def put(self):
        game_id = request.form["game_id"]
        group_ids = request.form["group_ids"]
        pickled_agent = request.files["agent"].read()

        # Check if the pickled file meeting our requirements
        agent = service.validate_pickle(pickled_agent)

        # Get the gym env and num of episodes to evaluate the agent on
        env = environment_service.find_env_by_game(game_id)
        game = game_service.find_game(game_id)

        # Evaluate the scores of the agent
        scores = service.evaluate_agent(agent, env.gym_env, game.num_of_episodes)

        # Save the agent with his score to the db
        inserted_id = service.submit_agent(game_id, group_ids, pickled_agent, scores)

        return jsonify({ "inserted_id": inserted_id })
    
    def get(self, student_id):
        result = service.find_submissions_by_student(student_id)
        
        return jsonify(result)