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
    
    def find_one(self, game_id):
        query = {'_id': game_id}
        self = db.db[Game.collection].find(query)
        return self
        # submissions_dict = get_submissions(game_id)
        # return game_dict.update(submissions_dict)

    def to_dict(self):
        return self.__dict__
