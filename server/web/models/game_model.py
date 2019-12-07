from datetime import datetime
from bson.objectid import ObjectId

from ..models.submission_model import Submission

class Game:

    collection = "games"

    def __init__(self, _id=None, name=None, env_id=None, due_date=None, num_of_episodes=None, submissions=None):

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

        if num_of_episodes is not None:
<<<<<<< HEAD
            self.num_of_episodes = int(num_of_episodes)
||||||| merged common ancestors
<<<<<<< HEAD
            self.num_of_episodes = int(num_of_episodes)
=======
            self.num_of_episodes = num_of_episodes
>>>>>>> 37bb70181f48cf5a40931d50a1311692efef8a4c
=======
            try:
                self.num_of_episodes = int(num_of_episodes)
            except ValueError:
                raise ValueError("Number of episodes is not a valid number.")
>>>>>>> de3f7df959f41026b7a9162e965acd4523f5b08b
            
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