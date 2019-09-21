from datetime import datetime
from bson.objectid import ObjectId

from .. import db

class Submission:

    collection = "submissions"

    def __init__(self, game_id, group_ids, agent, scores={"simpleAvg": 0}):
        self.game_id = game_id
        self.group_ids = group_ids
        self.agent = agent
        self.submission_date = datetime.now()
        self.scores = scores

    def insert_one(self):
        db.db[Submission.collection].insert_one(self.to_dict())

    def find_all_by_game(game_id):
        query = {
            "game_id": game_id#ObjectId(game_id)
        }

        submissions = db.db[Submission.collection].find(query)

    def set_score(self, name, score):
        self.scores[name] = score

    def to_dict(self):
        return self.__dict__