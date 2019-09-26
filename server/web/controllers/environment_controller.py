from flask import request
from flask import jsonify
from flask_restful import Resource

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

class Environments(Resource):
    def get(self):
        envs = service.find_all_envs()
        
        return jsonify(envs)