from .. import db

class Game:

    collection = "games"

    def __init__(self, game_name, env_id, due_date, num_of_episods):
        self.game_name = game_name
        self.env_id = env_id
        self.due_date = due_date
        self.num_of_episods = num_of_episods
        self.submissions = list()

    def set_submission(self, submission_id):
        self.submissions.append(submission_id)

    def insert_one(self):
        db.db[Game.collection].insert_one(self.to_dict())
    
    def find_game(self, game_id):
        query = {'_id': game_id}
        game_dict = db.db[Game.collection].find(query)
        session_dict = get_session(game_id)
        return game_dict.update(session_dict)

    def to_dict(self):
        return self.__dict__
