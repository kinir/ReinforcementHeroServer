import gym
import numpy as np
import dill
dill.settings['recurse'] = True


class Agent:
    def __init__(self, env):
        self.epsilon = 1
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.decay_rate = 0.00045
        self.lr_rate = 0.81
        self.gamma = 0.865

        self.action_space = env.action_space
        self.Q = np.zeros((env.observation_space.n, env.action_space.n))

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            action = self.action_space.sample()
        else:
            action = np.argmax(self.Q[state, :])

        return action
    
    def decay_epsilon(self, episode):
        self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * np.exp(-(self.decay_rate * episode))

    def learn(self, state, next_state, reward, action, done):
        predict = self.Q[state, action]

        if done:
            target  = reward
        else:
            target = reward + self.gamma * np.max(self.Q[next_state, :])

        self.Q[state, action] = self.Q[state, action] + self.lr_rate * (target - predict)

    def next_action(self, state):
        action = np.argmax(self.Q[state, :])
        return action


def main():
    env = gym.make('FrozenLake-v0')
    agent = Agent(env)

    episodes = 10000
    total_reward = 0

    for i in range(episodes):
        curr_state = env.reset()
        episode_reward = 0
        done = False

        while not done:
            # env.render()
            action = agent.choose_action(curr_state)
            next_state, reward, done, info = env.step(action)
            agent.learn(curr_state, next_state, reward, action, done)

            episode_reward += reward
            curr_state = next_state

        total_reward += episode_reward
        # env.render()

        if episode_reward == 1:
            agent.decay_epsilon(i)
        #print(agent.epsilon)
        #print(f"{i}) {total_reward}, {episode_reward}, {agent.epsilon}")
        print(total_reward / (i + 1))

    print(total_reward / episodes)
    #print(agent.Q)

    env.close()

    #save_agent(agent, episodes)


def save_agent(agent, episodes):
    with open(f"test_agents/pickles/FrozenLake8x8_QLearning{episodes}.pickle", 'wb') as f:
        dill.dump(agent, f)


if "__main__" == __name__:
    main()
