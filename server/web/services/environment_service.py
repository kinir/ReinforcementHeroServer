from .. import db
from ..models.environment_model import Environment

def insert_env(name, gym_env):
    env = Environment(
        name=name,
        gym_env=gym_env
    )

    db.db[Environment.collection].insert_one(env.to_dict())

def find_all_envs():
    return [Environment.from_dict(env) for env in db.db[Environment.collection].find()]