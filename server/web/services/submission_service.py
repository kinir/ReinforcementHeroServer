import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import gym
import dill
from datetime import datetime

from .. import database
from ..models.submission_model import Submission
from ..models.environment_model import Environment
from ..models.game_model import Game

def evaluate_agent(agent, gym_env, episodes):
    env = gym.make(gym_env)

    total_reward = 0
    for _ in range(episodes):
        curr_state = env.reset()
        episode_reward = 0
        done = False
        while not done:
            action = agent.next_action(curr_state)

            next_state, reward, done, _ = env.step(action)
            episode_reward += reward

            curr_state = next_state

        total_reward += episode_reward

    scores = {
        "simpleAvg": total_reward / episodes
    }

    return scores

def validate_pickle(pickled_agent):
    
    # Load agent instance from bytestream
    agent = dill.loads(pickled_agent)

    # Validate that the agent instance has next_action method
    if hasattr(agent, "next_action"):
        return agent
    else:
        raise Exception("Pickle file does not containt an agent of class 'Agent' or does not have next_action method.")

def submit_agent(game_id, group_ids, agent, scores):
    sub = Submission(
        game_id=game_id,
        group_ids=map(str.strip, group_ids.split(',')),
        agent=agent,
        submission_date=datetime.now(),
        scores=scores
    )

    return database.insert_one_submission(game_id, sub.to_dict())

def find_submissions_by_game(game_id):    
    submissions = [Submission.from_dict(sub) for sub in database.find_submissions_by_game(game_id)]

    return submissions

def find_submissions_by_student(student_id):
    submissions = [Submission.from_dict(sub) for sub in database.find_submissions_by_student(student_id, show_fields=["game_id",
                                                                                                                      "group_ids",
                                                                                                                      "submission_date",
                                                                                                                      "scores"])]

    return submissions