from flask import request
from flask_restful import Resource
from bson import json_util

from ..services import environment_service as service

class Environment(Resource):
    def put(self):
        try:
            name = request.form["name"]
            gym_env = request.form["gym_env"]
            
            service.insert_env(name, gym_env)
        
        except Exception as e:
            return repr(e)

        return True

    def get(self):

        # Fetch all the record(s)
        env_list = service.find_all_envs()
        return json_util.dumps(env_list)