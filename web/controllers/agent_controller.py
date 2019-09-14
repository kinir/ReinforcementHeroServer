from flask import request
from flask_restful import Resource

from ..services import agent_service as service

class Agent(Resource):
    def put(self):
        student_id = request.form["student_id"]
        env = request.form["env"]
        pickled_agent = request.files["agent"].read()
        
        try:

            # Check if the pickled file meeting our requirements
            agent = service.validate_pickle(pickled_agent)

            # Evaluate the average reward of the agent
            score = service.evaluate_agent(agent)

            # Save the agent with his score to the db
            service.submit_agent(None, None)
        except Exception as e:
            return repr(e)

        return score

    def get(self):
        try:
            service.save_to_db("Hello?!")
            return "Done!"
        except Exception as e:
            return repr(e)