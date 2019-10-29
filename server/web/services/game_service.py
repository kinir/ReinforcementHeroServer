from .. import database
from ..models.game_model import Game
from ..services import submission_service as submission_service

def insert_game(name, env_id, due_date, num_of_episods):
    game = Game(
        name=name,
        env_id=env_id,
        due_date=due_date,
        num_of_episods=num_of_episods
    )

    return database.insert_one(Game.collection, game.to_dict())

def find_game(game_id):
    game = Game.from_dict(list(database.find_single_game(game_id))[0])

    return game

def find_all_games():
    games = [Game.from_dict(game) for game in database.find_all_documents(Game.collection, show_fields=["_id", "name"])]

    return games
