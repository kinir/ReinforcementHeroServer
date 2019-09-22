import dill
import gym
from bson.objectid import ObjectId

from .. import db
from ..models.game_model import Game
from ..services import submission_service as submission_service

def insert_game(game_name, env_id, due_date, num_of_episods):
    game = Game(
        game_name=game_name,
        env_id=env_id,
        due_date=due_date,
        num_of_episods=num_of_episods)

    db.db[Game.collection].insert_one(game.to_dict())

def find_game(game_id):
    query = {
        "_id": ObjectId(game_id)
    }

    game = Game.from_dict(db.db[Game.collection].find_one(query))
    game.set_submissions(submission_service.find_submissions_by_game(game_id))

    return game
