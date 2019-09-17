class Game:
    def __init__(self, game_name, env_id, due_date, num_of_episods):
        self.game_name = game_name
        self.env_id = env_id
        self.due_date = due_date
        self.num_of_episods = num_of_episods
        self.submissions = list()

    def set_submission(self, submission_id):
        self.submissions.append(submission_id)
