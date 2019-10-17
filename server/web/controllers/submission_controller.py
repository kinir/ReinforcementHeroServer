from flask import request
from flask_restful import Resource
from flask import jsonify

from ..services import submission_service as service

class Submission(Resource):
    def put(self):
        
        try:
            game_id = request.form["game_id"]
            group_ids = request.form["group_ids"]
            pickled_agent = request.files["agent"].read()

            # Check if the pickled file meeting our requirements
            agent = service.validate_pickle(pickled_agent)

            # Evaluate the scores of the agent
            scores = service.evaluate_agent(agent)

            # Save the agent with his score to the db
            service.submit_agent(game_id, group_ids, pickled_agent, scores)

        except Exception as e:
            return repr(e)

        return True
    
    def get(self, student_id):
        result = service.find_submissions_by_student(student_id)
        
        return jsonify(result)