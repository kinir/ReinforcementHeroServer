from datetime import datetime
from bson.objectid import ObjectId

class Submission:

    collection = "submissions"

    def __init__(self, _id=0, game_id=0, group_ids=list(), agent="", submission_date=datetime.now(), scores={"simpleAvg": 0}):

        # Set only valid ids (for new submission there is no need for self generated id)
        if ObjectId.is_valid(_id):
            self._id = str(_id)
            
        if ObjectId.is_valid(game_id):
            self.game_id = game_id
        else:
            raise Exception("Game id is not a valid ObjectId.")
            
        self.group_ids = group_ids
        self.agent = agent
        self.submission_date = submission_date
        self.scores = scores

    def set_score(self, name, score):
        self.scores[name] = score

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return self.__dict__