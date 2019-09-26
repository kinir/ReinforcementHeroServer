from datetime import datetime
from bson.objectid import ObjectId

class Game:

    collection = "games"

    def __init__(self, _id=0, name="", env_id=0, due_date=datetime.now(), num_of_episods=10000, submissions=list()):

        # Set only valid ids (for new game there is no need for self generated id)
        if ObjectId.is_valid(_id):
            self._id = _id
            
        self.name = name

        if ObjectId.is_valid(env_id):
            self.env_id = env_id
        else:
            raise Exception("Invalid environment id.")

        self.due_date = datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%S")
        self.num_of_episods = num_of_episods
        self.submissions = self.set_submissions(submissions)

    def set_submissions(self, submissions):
        self.submissions = submissions

        # No need for and agent when returning a list of submissions
        for submission in self.submissions:
            del submission.agent

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return self.__dict__