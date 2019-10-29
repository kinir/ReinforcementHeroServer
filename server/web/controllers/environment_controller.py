from flask import request, jsonify, abort
from flask_restful import Resource

from ..services import environment_service as service

class Environment(Resource):
    def put(self):
        name = request.form["name"]
        gym_env = request.form["gym_env"]
        
        inserted_id = service.insert_env(name, gym_env)

        return jsonify({ "inserted_id": inserted_id })

class Environments(Resource):
    def get(self):
        envs = service.find_all_envs()
        
        return jsonify(envs)