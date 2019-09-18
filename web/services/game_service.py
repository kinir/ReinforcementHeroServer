import dill
import gym

from .. import db
from ..models.game_model import Game

def insert_game(game_name, env_id, due_date, num_of_episods):
    game = Game(game_name, env_id, due_date, num_of_episods)
    game.insert_one()

def find_game(query):
    return find_game(query)