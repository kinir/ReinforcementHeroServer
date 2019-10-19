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

    database.insert_one(Game.collection, game.to_dict())

def find_game(game_id):
    game = Game.from_dict(database.find_by_id(Game.collection, game_id))
    game.set_submissions(submission_service.find_submissions_by_game(game_id))

    return game

def find_all_games():
    games = [Game.from_dict(game) for game in database.find_all_documents(Game.collection, show_fields=["_id", "game"])]

    return games
