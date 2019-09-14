import gym
import numpy as np
import dill
dill.settings['recurse'] = True


class Agent:
    def __init__(self, env):
        self.epsilon = 0.9
        self.epsilon_decay = 0.99995
        self.lr_rate = 0.81
        self.gamma = 0.96
        self.action_space = env.action_space
        self.Q = np.zeros((env.observation_space.n, env.action_space.n))

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            print(self.epsilon)
            action = self.action_space.sample()
        else:
            action = np.argmax(self.Q[state, :])

        self.epsilon *= self.epsilon_decay

        return action

    def learn(self, state, next_state, reward, action):
        predict = self.Q[state, action]
        target = reward + self.gamma * np.max(self.Q[next_state, :])
        self.Q[state, action] = self.Q[state, action] + self.lr_rate * (target - predict)

    def next_action(self, state):
        action = np.argmax(self.Q[state, :])
        return action


def main():
    env = gym.make('FrozenLake-v0')
    agent = Agent(env)

    episodes = 5000
    total_reward = 0

    for i in range(episodes):
        curr_state = env.reset()
        episode_reward = 0
        done = False

        while not done:
            # env.render()
            action = agent.choose_action(curr_state)
            next_state, reward, done, info = env.step(action)
            agent.learn(curr_state, next_state, reward, action)

            episode_reward += reward
            curr_state = next_state

        total_reward += episode_reward
        # env.render()

    print(total_reward / episodes)
    print(agent.Q)

    env.close()

    save_agent(agent, episodes)


def save_agent(agent, episodes):
    with open(f"FrozenLake_QLearning{episodes}.pickle", 'wb') as f:
        dill.dump(agent, f)


if "__main__" == __name__:
    main()
