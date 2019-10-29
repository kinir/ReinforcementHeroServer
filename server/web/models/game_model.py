from datetime import datetime
from bson.objectid import ObjectId

from ..models.submission_model import Submission

class Game:

    collection = "games"

    def __init__(self, _id=None, name=None, env_id=None, due_date=None, num_of_episods=None, submissions=None):

        # Set only valid ids (for new game there is no need for self generated id)
        if ObjectId.is_valid(_id):
            self._id = _id
            
        if name is not None:
            self.name = name

        if env_id is not None:
            if ObjectId.is_valid(env_id):
                self.env_id = ObjectId(env_id)
            else:
                raise Exception("Environment id is not a valid ObjectId.")

        if due_date is not None:
            self.due_date = due_date

        if num_of_episods is not None:
            self.num_of_episods = num_of_episods
            
        if submissions is not None:
            self.set_submissions(submissions)

    def set_submissions(self, submissions):
        self.submissions = list()

        # No need for and agent when returning a list of submissions
        for submission in submissions:
            if not isinstance(submission, Submission):
                submission = Submission.from_dict(submission)
            
            del submission.agent
            self.submissions.append(submission)

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return self.__dict__