import gym
import gym_maze

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import dill
dill.settings['recurse'] = True


class RandomAgent:
    def __init__(self, env_name):
        env = gym.make(env_name)
        self.action_space = env.action_space

    def next_action(self, _):
        return self.action_space.sample()

    def get_pickled_agent(self):
        return dill.dumps(self)