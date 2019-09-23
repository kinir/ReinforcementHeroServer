from bson.objectid import ObjectId

class Environment:

    collection = "environments"

    def __init__(self, _id=0, name="", gym_env=""):
        # Set only valid ids (for new env there is no need for self generated id)
        if ObjectId.is_valid(_id):
            self._id = str(_id)
            
        self.name = name
        self.gym_env = gym_env

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return self.__dict__