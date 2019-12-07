from .. import database
from ..models.game_model import Game
from ..services import submission_service as submission_service
from ..services.random_agent import RandomAgent

def insert_game(name, env_id, due_date, num_of_episodes):
    game = Game(
        name=name,
        env_id=env_id,
        due_date=due_date,
        num_of_episodes=num_of_episodes
    )

    return database.insert_one(Game.collection, game.to_dict())

def find_game(game_id):
    game = Game.from_dict(list(database.find_single_game(game_id))[0])

    return game

def find_all_games():
    games = [Game.from_dict(game) for game in database.find_all_documents(Game.collection, show_fields=["_id", "name"])]

    return games

def submit_random_agent(game_id, gym_env):
    random_agent = RandomAgent(gym_env)

    # Evaluate the scores of the agent
    scores = submission_service.evaluate_agent(random_agent)

    # Save the agent with his score to the db
    inserted_id = submission_service.submit_agent(game_id, "random agent", random_agent.get_pickled_agent(), scores)