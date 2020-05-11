import gym
import gym_maze
import numpy as np
import dill
dill.settings['recurse'] = True

import os
os.environ['SDL_VIDEODRIVER']='dummy'

class Agent:
    def __init__(self, env):
        # Bounds for each discrete state
        self.STATE_BOUNDS = list(zip(env.observation_space.low, env.observation_space.high))
        # Number of discrete states (bucket) per state dimension
        MAZE_SIZE = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
        self.NUM_BUCKETS = MAZE_SIZE  # one bucket per grid

        self.epsilon = 1
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.decay_rate = 0.0005
        self.lr_rate = 0.81
        self.gamma = 0.96

        self.action_space = env.action_space

        # Number of discrete actions
        NUM_ACTIONS = env.action_space.n  # ["N", "S", "E", "W"]
        
        self.Q = np.zeros(self.NUM_BUCKETS + (NUM_ACTIONS,))

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            action = self.action_space.sample()
        else:
            action = int(np.argmax(self.Q[state]))

        return action
    
    def decay_epsilon(self, episode):
        self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * np.exp(-(self.decay_rate * episode))

    def learn(self, state, next_state, reward, action, done):
        # Update the Q based on the result
        best_q = np.amax(self.Q[next_state])
        self.Q[state + (action,)] += self.lr_rate * (reward + self.gamma * (best_q) - self.Q[state + (action,)])

    def state_to_bucket(self, state):
        bucket_indice = []
        for i in range(len(state)):
            if state[i] <= self.STATE_BOUNDS[i][0]:
                bucket_index = 0
            elif state[i] >= self.STATE_BOUNDS[i][1]:
                bucket_index = self.NUM_BUCKETS[i] - 1
            else:
                # Mapping the state bounds to the bucket array
                bound_width = self.STATE_BOUNDS[i][1] - self.STATE_BOUNDS[i][0]
                offset = (self.NUM_BUCKETS[i]-1)*self.STATE_BOUNDS[i][0]/bound_width
                scaling = (self.NUM_BUCKETS[i]-1)/bound_width
                bucket_index = int(round(scaling*state[i] - offset))
            bucket_indice.append(bucket_index)
        return tuple(bucket_indice)


    def next_action(self, state):
        action = int(np.argmax(self.Q[self.state_to_bucket(state)]))
        return action


def train_agent():
    env = gym.make('maze-sample-10x10-v0')
    agent = Agent(env)

    episodes = 100
    total_reward = 0

    for i in range(episodes):
        curr_state = env.reset()
        curr_state = agent.state_to_bucket(curr_state)
        episode_reward = 0
        done = False

        while not done:
            # env.render()
            action = agent.choose_action(curr_state)
            next_state, reward, done, info = env.step(action)
            next_state = agent.state_to_bucket(next_state)
            agent.learn(curr_state, next_state, reward, action, done)

            episode_reward += reward
            curr_state = next_state

        total_reward += episode_reward
        # env.render()

        agent.decay_epsilon(i)
        # print(agent.epsilon)
        print('Episode '+str(i)+'/'+str(episodes), end='\r')
        if i<10 or i==100 or i==1000 or i%10000==0:
          print(str(i)+' reward: '+str(episode_reward))

    print('Avg reward: '+str(total_reward / episodes))
    # print(agent.Q)

    env.close()

    save_agent(agent, episodes)


def save_agent(agent, episodes):
    with open(f"../Maze_QLearning{episodes}.pickle", 'wb') as f:
        dill.dump(agent, f)


train_agent()