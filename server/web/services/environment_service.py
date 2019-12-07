from .. import database
from ..models.environment_model import Environment

def insert_env(name, gym_env):
    env = Environment(
        name=name,
        gym_env=gym_env
    )

    return database.insert_one(Environment.collection, env.to_dict())

def find_all_envs():
    return [Environment.from_dict(env) for env in database.find_all_documents(Environment.collection)]

def find_env(env_id):
    env = Environment.from_dict(database.find_by_id(Environment.collection, env_id))

    return env