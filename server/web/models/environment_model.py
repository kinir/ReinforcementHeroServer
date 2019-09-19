from datetime import datetime

from .. import db

class Envinronment:

    collection = "envinronments"

    def __init__(self, name, gym_env):
        self.name = name
        self.gym_env = gym_env

    def insert_one(self):
        db.db[Envinronment.collection].insert_one(self.to_dict())

    def to_dict(self):
        return self.__dict__