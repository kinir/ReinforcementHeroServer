import sys
import numpy as np
import math
import random

import gym
import gym_maze
import dill
dill.settings['recurse']=True

class Agent:
    def __init__(self, env):
        self.learning_rate = 0.1
        self.epsilon = 0.95
        self.episodes = 100
        self.discount_factor = 0.99
        self.action_space = env.action_space
        self.MIN_EXPLORE_RATE = 0.001
        self.MIN_LEARNING_RATE = 0.2
        self.MAZE_SIZE = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
        self.NUM_ACTIONS = env.action_space.n
        self.STATE_BOUNDS = list(zip(env.observation_space.low, env.observation_space.high))

        self.START_EPSILON_DECAYING = 1
        self.END_EPSILON_DECAYING = self.episodes // 2
        self.epsilon_decay_value = self.epsilon / (self.END_EPSILON_DECAYING - self.START_EPSILON_DECAYING)
        self.DECAY_FACTOR = np.prod(self.MAZE_SIZE, dtype=float) / 10.0
        
        self.q_table = np.random.uniform(low=-2, high=0, size=(self.MAZE_SIZE + (env.action_space.n,)))

    def get_explore_rate(self, t):
        return max(self.MIN_EXPLORE_RATE, min(0.8, 1.0 - math.log10((t+1) / self.DECAY_FACTOR)))

    def get_learning_rate(self, t):
        return max(self.MIN_LEARNING_RATE, min(0.8, 1.0 - math.log10((t+1) / self.DECAY_FACTOR)))

    def next_step(self, state, explore_rate):
        if random.random() < explore_rate:
            action = self.action_space.sample()
        else:
            action = int(np.argmax(self.q_table[state]))

        return action

    def get_discrete_state(self, state):
        discrete_state = []
        for i in range(len(state)):
            if state[i] <= self.STATE_BOUNDS[i][0]:
                bucket_index = 0
            elif state[i] >= self.STATE_BOUNDS[i][1]:
                bucket_index = self.MAZE_SIZE[i] - 1
            else:
                offset = (self.MAZE_SIZE[i]-1) * self.STATE_BOUNDS[i][0] / self.STATE_BOUNDS[i][1] - self.STATE_BOUNDS[i][0]
                scaling = (self.MAZE_SIZE[i]-1) / self.STATE_BOUNDS[i][1] - self.STATE_BOUNDS[i][0]
                bucket_index = int(round(scaling*state[i] - offset))
            discrete_state.append(bucket_index)
        return tuple(discrete_state)

    def next_action(self, state):
        action = int(np.argmax(self.q_table[self.get_discrete_state(state)]))
        return action


def main():
    env = gym.make("maze-sample-10x10-v0")
    env.reset()
    agent = Agent(env)
    learning_rate = agent.get_learning_rate(0)
    explore_rate = agent.get_explore_rate(0)
    for episode in range(agent.episodes):
        count_steps = 0
        obv = env.reset()

        start_state = agent.get_discrete_state(obv)
        total_reward = 0

        game_over = False

        while not game_over:
            env.render()
            count_steps = count_steps + 1
            action = agent.next_step(start_state, explore_rate)
            new_state, reward, game_over, _ = env.step(action)
            state = agent.get_discrete_state(new_state)
            total_reward += reward

            best_q = np.amax(agent.q_table[state])
            agent.q_table[start_state + (action,)] += learning_rate * (reward + agent.discount_factor * (best_q) - agent.q_table[start_state + (action,)])

            start_state = state

            if agent.END_EPSILON_DECAYING >= episode >= agent.START_EPSILON_DECAYING:
                agent.epsilon -= agent.epsilon_decay_value

        print('steps: ', count_steps)

        env.close()
    print(total_reward / (agent.episodes + 1))

    with open(f"./q_maze.pickle", 'wb') as f:
        dill.dump(agent, f)

if "__main__" == __name__:
    main()