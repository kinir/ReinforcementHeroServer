from datetime import datetime
from bson.objectid import ObjectId

class Game:

    collection = "games"

    def __init__(self, _id=0, env_id=0, game_name="", due_date=datetime.now(), num_of_episods=10000, submissions=list()):

        # Set only valid ids (for new game there is no need for self generated id)
        if ObjectId.is_valid(_id):
            self._id = _id
            
        self.env_id = env_id
        self.game_name = game_name
        self.due_date = due_date
        self.num_of_episods = num_of_episods
        self.submissions = submissions

    def set_submissions(self, submissions):
        self.submissions = submissions

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return self.__dict__