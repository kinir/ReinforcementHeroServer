from datetime import datetime
from bson.objectid import ObjectId

class Submission:

    collection = "submissions"

    def __init__(self, _id=None, game_id=None, group_ids=None, agent=None, submission_date=datetime.now(), scores={"simpleAvg": 0}):
            
        # Set only valid ids (for new submission there is no need for self generated id)
        if ObjectId.is_valid(_id):
            self._id = str(_id)
            
        if ObjectId.is_valid(game_id):
            self.game_id = game_id
        else:
            raise Exception("Game id is not a valid ObjectId.")

        if group_ids is not None:    
            self.group_ids = group_ids
        
        if agent is not None:
            self.agent = agent
        
        if submission_date is not None:
            self.submission_date = submission_date

        if scores is not None:
            self.scores = scores

    def set_score(self, name, score):
        self.scores[name] = score

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return self.__dict__