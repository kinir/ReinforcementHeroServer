from datetime import datetime

class Submission:
    def __init__(self, game_id, group_ids, agent):
        self.game_id = game_id
        self.group_ids = group_ids
        self.agent = agent
        self.submission_date = datetime.now()
        self.rewards = {
            "simpleAvg": 0
        }